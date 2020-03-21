import networkx as nx 
import matplotlib.pyplot as plt

from gui.interface import send_data

population = []

def populate_graph():
    population = send_data()
    graph = nx.MultiDiGraph()
    #nodes=(person.name for person in population)
    names = []
    for person in population:
        names.append(person.name)
    graph.add_nodes_from(names)
    for person in population:
        if person.father is not None:
            #print("name & father:", person.name, person.father,"\n")
            graph.add_edge(person.name, person.father)
        if person.mother is not None:
            #print("name & mother:", person.name, person.mother,"\n")
            graph.add_edge(person.name, person.mother)
        if person.child1 is not None:
            #print("ch1 & name:", person.child1, person.name,"\n")
            graph.add_edge(person.child1, person.name)
        if person.child2 is not None:
           # print("ch2 & name:", person.child2, person.name,"\n")
            graph.add_edge(person.child2, person.name)
        if person.child3 is not None:
            #print("ch3 & name:", person.child3, person.name,"\n")
            graph.add_edge(person.child3, person.name)


def calculate_inbreed(graph, child):
    parents=nx.dfs_tree(graph, source=child, depth_limit=1)
    print("rodzice", list(parents))
    # paths = nx.all_simple_paths(graph, source="person_K", target="person_I")
    # parents1 = list(nx.descendants(graph, source="person_K"))
    # parents2 = list(nx.descendants(graph, source="person_I"))
    # print("Parents K", parents1)
    # print("Parents I", parents2)
    # res = [val for key, val in enumerate(parents1) if val in set(parents2)]     
    # print("Wspolni przodkowie: ", res)

    # paths1 = nx.all_simple_paths(graph, source="person_K", target="person_A")
    # paths21 = nx.all_simple_paths(graph, source="person_I", target="person_A")
    # print("Sciezki dla K, I do A: ", list(paths1), list(paths21))
    # paths2 = nx.all_simple_paths(graph, source="person_K", target="person_B")
    # paths22 = nx.all_simple_paths(graph, source="person_I", target="person_B")
    # print("Sciezki dla K, I do B: ", list(paths2), list(paths22))
    # paths3 = nx.all_simple_paths(graph, source="person_K", target="person_C")
    # paths23 = nx.all_simple_paths(graph, source="person_I", target="person_C")
    # print("Sciezki dla K, I do C: ", list(paths3), list(paths23))
    

    pos=nx.kamada_kawai_layout(graph)
    nx.draw(graph, pos=pos, node_color="yellow")
    nx.draw_networkx_labels(graph, pos=pos)
    plt.show()