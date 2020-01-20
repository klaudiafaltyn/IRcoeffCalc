import networkx as nx 
import matplotlib.pyplot as plt

from gui.interface import send_data

population = []

def populate_graph():
    population = send_data()
    tree = nx.MultiDiGraph()
    #nodes=(person.name for person in population)
    names = []
    for person in population:
        names.append(person.name)
    tree.add_nodes_from(names)
    for person in population:
        if person.father is not None:
            #print("name & father:", person.name, person.father,"\n")
            tree.add_edge(person.name, person.father)
        if person.mother is not None:
            #print("name & mother:", person.name, person.mother,"\n")
            tree.add_edge(person.name, person.mother)
        if person.child1 is not None:
            #print("ch1 & name:", person.child1, person.name,"\n")
            tree.add_edge(person.child1, person.name)
        if person.child2 is not None:
           # print("ch2 & name:", person.child2, person.name,"\n")
            tree.add_edge(person.child2, person.name)
        if person.child3 is not None:
            #print("ch3 & name:", person.child3, person.name,"\n")
            tree.add_edge(person.child3, person.name)
    
    pos=nx.kamada_kawai_layout(tree)
    nx.draw(tree, pos=pos, node_color="yellow")
    nx.draw_networkx_labels(tree, pos=pos)
    plt.show()