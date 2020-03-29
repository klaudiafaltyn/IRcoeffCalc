import networkx as nx 
import matplotlib.pyplot as plt
from math import sqrt

population = []
graph_wrapper = []

def populate_graph():
    graph = nx.MultiDiGraph()
    graph.add_nodes_from([person.name for person in population])
    for person in population:
        if person.father is not None and not graph.has_edge(person.name, person.father):
            graph.add_edge(person.name, person.father)
        if person.mother is not None and not graph.has_edge(person.name, person.mother):
            graph.add_edge(person.name, person.mother)
        for child in person.children:
            graph.add_edge(child, person.name)
    return graph

def inbreed_calculate(child):
    graph = graph_wrapper[0]   
    
    # Storing only relevant parts of graph 
    edges = []
    nodes = []

    # Retriving parents nodes
    parents = list(nx.dfs_tree(graph, source=child, depth_limit=1))
    
    if len(parents) != 3:
        return 0

    edges.extend( [(child, parents[1]), (child, parents[2]) ] )
    nodes.extend(parents)



    # Diffrent, possible better approach XD    
    # nx.draw(graph_wrapper[0],edgelist=edges, nodelist=nodes, pos=pos, node_color="yellow")
    # nx.draw_networkx_labels(graph_wrapper[0], pos=pos)
    # plt.show()


    parents.remove(child)
    parent1_ancestors = list(nx.descendants(graph, source=parents[0]))
    parent2_ancestors = list(nx.descendants(graph, source=parents[1]))
    common_ancestors = [val for val in parent1_ancestors if val in parent2_ancestors]     
    
    nodes.extend(common_ancestors)

    inbreeding_coefficient = 0
    for ancestor in list(common_ancestors):
        paths_to_ancestor_par1 = list(nx.all_simple_paths(graph, source=parents[0], target=ancestor))
        paths_to_ancestor_par2 = list(nx.all_simple_paths(graph, source=parents[1], target=ancestor))
        for paths1 in paths_to_ancestor_par1:
            for paths2 in paths_to_ancestor_par2:
                if len([node for node in paths1 if node in paths2]) == 1:  
                    inbreeding_coefficient += (0.5)**(len(paths1)+len(paths2)- 2 + 1)*(1+inbreed_calculate(ancestor))
    


    # pos=nx.kamada_kawai_layout(graph)
    # nx.draw_networkx_nodes(graph, pos=pos, nodelist=nodes, node_color='b') #or even nx.draw(h,pos=pos,node_color='b') to get nodes and edges in one command
    # nx.draw_networkx_edges(graph, pos=pos, edgelist=edges)
    # plt.show()
    return inbreeding_coefficient


def relation_calculate(child1, child2):
    graph = graph_wrapper[0]

    parents = [child1, child2]
    


    parent1_ancestors = list(nx.descendants(graph, source=parents[0]))
    parent2_ancestors = list(nx.descendants(graph, source=parents[1]))
    common_ancestors = [val for _, val in enumerate(parent1_ancestors) if val in set(parent2_ancestors)]     
    
    numerator = 0.0
    for ancestor in list(common_ancestors):
        paths_to_ancestor_par1 = list(nx.all_simple_paths(graph, source=parents[0], target=ancestor))
        paths_to_ancestor_par2 = list(nx.all_simple_paths(graph, source=parents[1], target=ancestor))
        for paths1 in paths_to_ancestor_par1:
            for paths2 in paths_to_ancestor_par2:
                if len([node for node in paths1 if node in paths2]) == 1:  
                    numerator += (0.5)**(len(paths1)+len(paths2)- 2 )*(1+inbreed_calculate(ancestor))
    
    denominator = sqrt( (1.0 + inbreed_calculate(child1))* (1.0 + inbreed_calculate(child2)) )
    return numerator/denominator

#    numerator  -   licznik
#   -----------    --------- !!!!!!!!!!!!!!!!!
#   denominator -  mianownik


def generate_data(data):
    if len(population) != 0:
        population[:] = []
    for person in data:
        population.append(person)
    if len(graph_wrapper) != 0:
        graph_wrapper[:] = []
    graph_wrapper.append(populate_graph())


def draw_graph():
    if len(graph_wrapper) == 15:
        pos = nx.spring_layout(graph_wrapper[0], iterations=10)
        nx.draw(graph_wrapper[0], pos, node_size=0, alpha=0.4, edge_color='r', font_size=16, with_labels=True)
        plt.show()
        
        # pos=nx.kamada_kawai_layout(graph_wrapper[0])
        # nx.draw(graph_wrapper[0], pos=pos, node_color="yellow")
        # nx.draw_networkx_labels(graph_wrapper[0], pos=pos)
        # plt.show()
        
        # pos = hierarchy_pos(graph_wrapper[0],1)    
        # nx.draw(graph_wrapper[0], pos=pos, with_labels=True)
        # plt.show()
        # plt.savefig('hierarchy.png')