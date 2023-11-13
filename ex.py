import networkx as nx
import random
import time
import matplotlib.pyplot as plt


def greedy_max_cut(graph, num_iterations):
    best_cut_size = 0
    best_partition = None
    operations_counter = 0

    for _ in range(num_iterations):
        partition, oper_1 = random_partition(graph)
        cut_size, oper_2 = calculate_cut_size(graph, partition)
        operations_counter += (oper_1 + oper_2)

        if cut_size > best_cut_size:
            operations_counter += 1
            best_cut_size = cut_size
            best_partition = partition

    return best_partition, best_cut_size, num_iterations*operations_counter


def random_partition(graph):
    number_operations = 0
    partition = {}
    for node in graph.nodes():
        number_operations += 1
        partition[node] = random.choice(["S", "T"])
    return partition, number_operations


def calculate_cut_size(graph, partition):
    cut_size = 0
    number_operations = 0

    for edge in graph.edges():
        number_operations += 1
        if partition[edge[0]] != partition[edge[1]]:
            number_operations += 1
            cut_size += 1
    return cut_size, number_operations


def exhaustive_max_cut(graph):
    best_cut_size = 0
    best_partition = None
    loop_counter = 0
    operations_counter = 0

    for i in range(2 ** len(graph.nodes())):
        loop_counter += 1
        partition = {}
        bin_i = bin(i)[2:].zfill(len(graph.nodes()))

        for j, node in enumerate(graph.nodes()):
            partition[node] = "S" if bin_i[j] == "0" else "T"

        cut_size, oper = calculate_cut_size(graph, partition)

        operations_counter += oper

        if cut_size > best_cut_size:
            operations_counter += 1
            best_cut_size = cut_size
            best_partition = partition

    return best_partition, best_cut_size, loop_counter*operations_counter


def temporal_analysis_vertex():
    number_vertex = [vertex for vertex in range(4, 28)]
    times_exhaustive = []
    times_greedy = []
    operations_exhaustive = []
    operations_greedy = []

    for i in number_vertex:
        graph = nx.fast_gnp_random_graph(i,0.3,seed = 118377, directed = False)

        with open("results.txt", "a") as file:
            file.write("Graph: {}\n\n".format(graph.edges))

        start_time = time.perf_counter()
        best_partition, best_cut_size, oper = exhaustive_max_cut(graph)
        end_time = time.perf_counter()
        times_exhaustive.append((end_time - start_time))
        operations_exhaustive.append(oper)
        list_S = []
        list_T = []

        for key, value in best_partition.items():
            if value == "S":
                list_S.append(key)
            elif value == "T":
                list_T.append(key)
        print("\nExhaustive:")
        print("Best Cut Size:", best_cut_size)
        print("Best Partition:")
        print("\tSet S: ", list_S)
        print("\tSet T: ", list_T)
        print("Graph size (vertex): ", i)
        print("Duration: ", (end_time - start_time))
        print("Operations: ", oper)
        # write results to file
        with open("results.txt", "a") as file:
            file.write("Exhaustive:\n")
            file.write("Best Cut Size: {}\n".format(best_cut_size))
            file.write("Best Partition:\n")
            file.write("\tSet S: {}\n".format(list_S))
            file.write("\tSet T: {}\n".format(list_T))
            file.write("Graph size (vertex): {}\n\n".format(i))
            file.write("Duration: {}\n\n".format(end_time - start_time))
            file.write("Operations: {}\n\n".format(oper))

        start_time = time.perf_counter()
        best_partition, best_cut_size, oper = greedy_max_cut(graph, 1000)
        end_time = time.perf_counter()
        times_greedy.append((end_time - start_time))
        operations_greedy.append(oper)
        list_S = []
        list_T = []

        for key, value in best_partition.items():
            if value == "S":
                list_S.append(key)
            elif value == "T":
                list_T.append(key)
        print("\nGreedy:")
        print("Best Cut Size:", best_cut_size)
        print("Best Partition:")
        print("\tSet S: ", list_S)
        print("\tSet T: ", list_T)
        print("Graph size (vertex): ", i)
        print("Duration: ", (end_time - start_time))
        print("Operations: ", oper)
        # write results to file
        with open("results.txt", "a") as file:
            file.write("Greedy:\n")
            file.write("Best Cut Size: {}\n".format(best_cut_size))
            file.write("Best Partition:\n")
            file.write("\tSet S: {}\n".format(list_S))
            file.write("\tSet T: {}\n".format(list_T))
            file.write("Graph size (vertex): {}\n\n".format(i))
            file.write("Duration: {}\n".format(end_time - start_time))
            file.write("Operations: {}\n".format(oper))
            file.write("\n\n=====================================================\n\n")

        print("\n\n=====================================================\n\n")

    plt.plot(number_vertex, operations_exhaustive, label='Exhaustive')
    plt.plot(number_vertex, operations_greedy, label='Greedy')
    plt.xlabel('Graph Size')
    plt.ylabel('Number of Operations')
    plt.title('Performance of Algorithms (Operations)')
    plt.legend()
    plt.show()

    plt.plot(number_vertex, times_exhaustive, label='Exhaustive')
    plt.plot(number_vertex, times_greedy, label='Greedy')
    plt.xlabel('Graph Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Performance of Algorithms (Time)')
    plt.legend()
    plt.show()

def temporal_analysis_edges():
    edge_probability = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    times_exhaustive = []
    times_greedy = []
    operations_exhaustive = []
    operations_greedy = []

    for i in edge_probability:
        graph = nx.fast_gnp_random_graph(18,i,seed = 118377, directed = False)

        with open("results.txt", "a") as file:
            file.write("Graph: {}\n\n".format(graph.edges))

        start_time = time.perf_counter()
        best_partition, best_cut_size, oper = exhaustive_max_cut(graph)
        end_time = time.perf_counter()
        times_exhaustive.append((end_time - start_time))
        operations_exhaustive.append(oper)
        list_S = []
        list_T = []

        for key, value in best_partition.items():
            if value == "S":
                list_S.append(key)
            elif value == "T":
                list_T.append(key)
        print("\nExhaustive:")
        print("Best Cut Size:", best_cut_size)
        print("Best Partition:")
        print("\tSet S: ", list_S)
        print("\tSet T: ", list_T)
        print("Edge probability: ", i)
        print("Graph size (edge): ", graph.number_of_edges())
        print("Duration: ", (end_time - start_time))
        print("Operations: ", oper)
        # write results to file
        with open("results.txt", "a") as file:
            file.write("Exhaustive:\n")
            file.write("Best Cut Size: {}\n".format(best_cut_size))
            file.write("Best Partition:\n")
            file.write("\tSet S: {}\n".format(list_S))
            file.write("\tSet T: {}\n".format(list_T))
            file.write("Edge probability: {}\n\n".format(i))
            file.write("Graph size (edge): {}\n\n".format(graph.number_of_edges()))
            file.write("Duration: {}\n\n".format(end_time - start_time))
            file.write("Operations: {}\n\n".format(oper))

        start_time = time.perf_counter()
        best_partition, best_cut_size, oper = greedy_max_cut(graph, 1000)
        end_time = time.perf_counter()
        times_greedy.append((end_time - start_time))
        operations_greedy.append(oper)
        list_S = []
        list_T = []

        for key, value in best_partition.items():
            if value == "S":
                list_S.append(key)
            elif value == "T":
                list_T.append(key)
        print("\nGreedy:")
        print("Best Cut Size:", best_cut_size)
        print("Best Partition:")
        print("\tSet S: ", list_S)
        print("\tSet T: ", list_T)
        print("Edge probability: ", i)
        print("Graph size (edge): ", graph.number_of_edges())
        print("Duration: ", (end_time - start_time))
        print("Operations: ", oper)
        # write results to file
        with open("results.txt", "a") as file:
            file.write("Greedy:\n")
            file.write("Best Cut Size: {}\n".format(best_cut_size))
            file.write("Best Partition:\n")
            file.write("\tSet S: {}\n".format(list_S))
            file.write("\tSet T: {}\n".format(list_T))
            file.write("Edge probability: {}\n\n".format(i))
            file.write("Graph size (edge): {}\n\n".format(graph.number_of_edges()))
            file.write("Duration: {}\n".format(end_time - start_time))
            file.write("Operations: {}\n".format(oper))
            file.write("\n\n=====================================================\n\n")

        print("\n\n=====================================================\n\n")

    plt.plot(edge_probability, operations_exhaustive, label='Exhaustive')
    plt.plot(edge_probability, operations_greedy, label='Greedy')
    plt.xlabel('Graph Size')
    plt.ylabel('Number of Operations')
    plt.title('Performance of Algorithms (Operations)')
    plt.legend()
    plt.show()

    plt.plot(edge_probability, times_exhaustive, label='Exhaustive')
    plt.plot(edge_probability, times_greedy, label='Greedy')
    plt.xlabel('Graph Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Performance of Algorithms (Time)')
    plt.legend()
    plt.show()

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

temporal_analysis_edges()


""" random_generate = input("Generate a random graph? (y/n)")

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
 """