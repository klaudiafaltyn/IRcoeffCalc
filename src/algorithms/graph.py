import os
import networkx as nx
import matplotlib.pyplot as plt
from math import sqrt

population = []
graph_wrapper = []


def find_name(arr, name):
    for person in arr:
        if person.name == name:
            return person


def populate_graph():
    graph = nx.DiGraph()
    graph.add_nodes_from(population)
    for person in population:
        if person.father is not None:
            graph.add_edge(person, find_name(population, person.father))
        if person.mother is not None:
            graph.add_edge(person, find_name(population, person.mother))
    return graph


def inbreed_calculate(child):
    graph = graph_wrapper[0]

    edges = []
    nodes = []

    parents = list(nx.dfs_tree(graph, source=child, depth_limit=1))

    if len(parents) != 3:
        return 0

    edges.extend([(child, parents[1]), (child, parents[2])])
    nodes.extend(parents)

    parents.remove(child)
    parent1_ancestors = list(nx.descendants(graph, source=parents[0]))
    parent2_ancestors = list(nx.descendants(graph, source=parents[1]))
    common_ancestors = [val for val in parent1_ancestors if val in parent2_ancestors]

    nodes.extend(common_ancestors)

    inbreeding_coefficient = 0
    for ancestor in list(common_ancestors):
        paths_to_ancestor_par1 = list(
            nx.all_simple_paths(graph, source=parents[0], target=ancestor)
        )
        paths_to_ancestor_par2 = list(
            nx.all_simple_paths(graph, source=parents[1], target=ancestor)
        )

        for paths1 in paths_to_ancestor_par1:
            for paths2 in paths_to_ancestor_par2:
                if len([node for node in paths1 if node in paths2]) == 1:
                    inbreeding_coefficient += (0.5) ** (
                        len(paths1) + len(paths2) - 2 + 1
                    ) * (1 + inbreed_calculate(ancestor))
    return inbreeding_coefficient


def relation_calculate(child1, child2):
    graph = graph_wrapper[0]

    parents = [child1, child2]

    parent1_ancestors = list(nx.descendants(graph, source=parents[0]))
    parent2_ancestors = list(nx.descendants(graph, source=parents[1]))
    common_ancestors = [
        val for _, val in enumerate(parent1_ancestors) if val in set(parent2_ancestors)
    ]

    numerator = 0.0
    for ancestor in list(common_ancestors):
        paths_to_ancestor_par1 = list(
            nx.all_simple_paths(graph, source=parents[0], target=ancestor)
        )
        paths_to_ancestor_par2 = list(
            nx.all_simple_paths(graph, source=parents[1], target=ancestor)
        )
        for paths1 in paths_to_ancestor_par1:
            for paths2 in paths_to_ancestor_par2:
                if len([node for node in paths1 if node in paths2]) == 1:
                    numerator += (0.5) ** (len(paths1) + len(paths2) - 2) * (
                        1 + inbreed_calculate(ancestor)
                    )

    denominator = sqrt(
        (1.0 + inbreed_calculate(child1)) * (1.0 + inbreed_calculate(child2))
    )
    return numerator / denominator


def generate_data(data):
    if len(population) != 0:
        population[:] = []
    for person in data:
        population.append(person)
    if len(graph_wrapper) != 0:
        graph_wrapper[:] = []
    graph_wrapper.append(populate_graph())


def draw_graph():
    if len(graph_wrapper) == 1:
        reversed_graph = nx.reverse(graph_wrapper[0], copy=True)
        if os.name == "nt":
            pos = nx.circular_layout(reversed_graph, prog="dot")
        else:
            pos = nx.nx_pydot.graphviz_layout(reversed_graph, prog="dot")
        nx.draw(
            reversed_graph,
            pos,
            with_labels=True,
            arrows=True,
            node_color="steelblue",
            alpha=0.6,
            node_size=100,
        )
        plt.show()
