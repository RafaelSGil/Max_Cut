import networkx as nx
import random
from datetime import datetime
import matplotlib.pyplot as plt


def greedy_max_cut(graph, num_iterations):
    best_cut_size = 0
    best_partition = None

    for _ in range(num_iterations):
        partition = random_partition(graph)
        cut_size = calculate_cut_size(graph, partition)

        if cut_size > best_cut_size:
            best_cut_size = cut_size
            best_partition = partition

    return best_partition, best_cut_size


def random_partition(graph):
    partition = {}
    for node in graph.nodes():
        partition[node] = random.choice(["A", "B"])
    return partition


def calculate_cut_size(graph, partition):
    cut_size = 0
    for edge in graph.edges():
        if partition[edge[0]] != partition[edge[1]]:
            cut_size += 1
    return cut_size


def exhaustive_max_cut(graph):
    best_cut_size = 0
    best_partition = None

    for i in range(2 ** len(graph.nodes())):
        partition = {}
        bin_i = bin(i)[2:].zfill(len(graph.nodes()))

        for j, node in enumerate(graph.nodes()):
            partition[node] = "A" if bin_i[j] == "0" else "B"

        cut_size = calculate_cut_size(graph, partition)

        if cut_size > best_cut_size:
            best_cut_size = cut_size
            best_partition = partition

    return best_partition, best_cut_size


# graph = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 3), (3, 4)]
# graph = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 3), (3, 4)]
graph = [
    (0, 1),
    (0, 12),
    (0, 7),
    (1, 8),
    (1, 7),
    (1, 8),
    (1, 2),
    (2, 7),
    (2, 3),
    (3, 4),
    (3, 7),
    (3, 9),
    (3, 5),
    (4, 5),
    (5, 6),
    (7, 8),
    (7, 10),
    (8, 11),
    (9, 10),
    (10, 11),
    (10, 12),
    (12, 13),
    (13, 14),
    (14, 15),
    (14, 17),
    (14, 18),
    (15, 16),
    (16, 17),
    (17, 18),
    (18, 13),
]


num_iterations = 1000

random_generate = input("Generate a random graph? (y/n)")

if random_generate == "y":
    num_vertex = input("How many vertex do you want to use? (up to 100)")
    prob_edges = input("What's the probability of making an edge? (up to 1)")
    graph = nx.erdos_renyi_graph(int(num_vertex), float(prob_edges))

    with open("results.txt", "a") as file:
        file.write("Graph: {}\n\n".format(graph.edges))

    start_time = datetime.now()
    best_partition, best_cut_size = exhaustive_max_cut(graph)
    end_time = datetime.now()
    list_A = []
    list_B = []

    for key, value in best_partition.items():
        if value == "A":
            list_A.append(key)
        elif value == "B":
            list_B.append(key)
    print("Exhaustive:")
    print("Best Cut Size:", best_cut_size)
    print("Best Partition:")
    print("\tSet A: ", list_A)
    print("\tSet B: ", list_B)
    print("Duration: {}".format(end_time - start_time))
    # write results to file
    with open("results.txt", "a") as file:
        file.write("Exhaustive:\n")
        file.write("Best Cut Size: {}\n".format(best_cut_size))
        file.write("Best Partition:\n")
        file.write("\tSet A: {}\n".format(list_A))
        file.write("\tSet B: {}\n".format(list_B))
        file.write("Duration: {}\n\n".format(end_time - start_time))

    start_time = datetime.now()
    best_partition, best_cut_size = greedy_max_cut(graph, num_iterations)
    end_time = datetime.now()
    list_A = []
    list_B = []

    for key, value in best_partition.items():
        if value == "A":
            list_A.append(key)
        elif value == "B":
            list_B.append(key)
    print("\nGreedy:")
    print("Best Cut Size:", best_cut_size)
    print("Best Partition:")
    print("\tSet A: ", list_A)
    print("\tSet B: ", list_B)
    print("Duration: {}".format(end_time - start_time))
    # write results to file
    with open("results.txt", "a") as file:
        file.write("Greedy:\n")
        file.write("Best Cut Size: {}\n".format(best_cut_size))
        file.write("Best Partition:\n")
        file.write("\tSet A: {}\n".format(list_A))
        file.write("\tSet B: {}\n".format(list_B))
        file.write("Duration: {}\n".format(end_time - start_time))
        file.write("\n\n=====================================================\n\n")

    nx.draw(graph)
    plt.show()

else:
    G = nx.Graph()
    G.add_edges_from(graph)

    with open("results.txt", "a") as file:
        file.write("Graph: {}\n\n".format(graph))

    start_time = datetime.now()
    best_partition, best_cut_size = exhaustive_max_cut(G)
    end_time = datetime.now()
    list_A = []
    list_B = []

    for key, value in best_partition.items():
        if value == "A":
            list_A.append(key)
        elif value == "B":
            list_B.append(key)
    print("Exhaustive:")
    print("Best Cut Size:", best_cut_size)
    print("Best Partition:")
    print("\tSet A: ", list_A)
    print("\tSet B: ", list_B)
    print("Duration: {}".format(end_time - start_time))
    # write results to file
    with open("results.txt", "a") as file:
        file.write("Exhaustive:\n")
        file.write("Best Cut Size: {}\n".format(best_cut_size))
        file.write("Best Partition:\n")
        file.write("\tSet A: {}\n".format(list_A))
        file.write("\tSet B: {}\n".format(list_B))
        file.write("Duration: {}\n\n".format(end_time - start_time))

    start_time = datetime.now()
    best_partition, best_cut_size = greedy_max_cut(G, num_iterations)
    end_time = datetime.now()
    list_A = []
    list_B = []

    for key, value in best_partition.items():
        if value == "A":
            list_A.append(key)
        elif value == "B":
            list_B.append(key)
    print("\nGreedy:")
    print("Best Cut Size:", best_cut_size)
    print("Best Partition:")
    print("\tSet A: ", list_A)
    print("\tSet B: ", list_B)
    print("Duration: {}".format(end_time - start_time))
    # write results to file
    with open("results.txt", "a") as file:
        file.write("Greedy:\n")
        file.write("Best Cut Size: {}\n".format(best_cut_size))
        file.write("Best Partition:\n")
        file.write("\tSet A: {}\n".format(list_A))
        file.write("\tSet B: {}\n".format(list_B))
        file.write("Duration: {}\n".format(end_time - start_time))
        file.write("\n\n=====================================================\n\n")

    nx.draw(G)
    plt.show()
