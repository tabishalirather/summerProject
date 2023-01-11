from itertools import combinations
import numpy as np


def generate_biconnected_graphs_4_vertices():
    # Initialize the list of adjacency matrices
    adj_mats = []

    # Generate all combinations of edges in the complete graph
    edges = combinations(range(4), 2)
    edges = list(edges)

    # Iterate over all edges
    for u, v in edges:
        # Create a complete graph with 5 vertices
        adj_mat = [[0 for _ in range(4)] for _ in range(4)]
        for i, j in edges:
            adj_mat[i][j] = 1
            adj_mat[j][i] = 1

        # Remove the edge (u, v)
        adj_mat[u][v] = 0
        adj_mat[v][u] = 0

        # Check if the graph is biconnected
        is_biconnected = True
        visited = [False] * 4
        low = [0] * 4
        disc = [0] * 4
        timestamp = 0

        def dfs(v, parent):
            nonlocal is_biconnected, timestamp
            visited[v] = True
            disc[v] = low[v] = timestamp
            timestamp += 1
            children = 0
            for u in range(4):
                if adj_mat[v][u] == 1:
                    if not visited[u]:
                        children += 1
                        dfs(u, v)
                        low[v] = min(low[v], low[u])
                        if parent != -1 and low[u] >= disc[v]:
                            is_biconnected = False
                    elif u != parent:
                        low[v] = min(low[v], disc[u])

        dfs(0, -1)
        if is_biconnected:
            adj_mats.append(adj_mat)

    return adj_mats


def permute(arr):
    from itertools import permutations
    # Generate all permutations of the list
    perms = list(permutations(arr))
    # print("All permutations")
    result = []
    for perm in perms:
        # print(perm)
        result.append(perm)
    return result


def printBiconnected():
    biconnected_graphs = generate_biconnected_graphs_4_vertices()
    for i, graph in enumerate(biconnected_graphs):
        print(f'Graph {i + 1}')
        for row in graph:
            print(row)


def printAllBiconnectedGraphs():
    biconnected_graphs = generate_biconnected_graphs_4_vertices()
    config = [1, 3, 2, 4, ]
    allConfigs = permute(config)
    # for config in allConfigs:
    # print(config)
    for graph in biconnected_graphs:
        # //insert first row and integers
        graph.insert(0, [0] + list(range(1, 6)))
        for i in range(1, 6):
            # inserts first columns and integers
            graph[i].insert(0, i)
    arrayOfGraphs = []
    simgaCount = 0
    for i, graph in enumerate(biconnected_graphs):
        print(f'Graph {i + 1}')
        for config in allConfigs:
            if (graph[config[0]][config[4]] == 1):
                # //check for one particular graphs and then for others
                print(config)
                print("simga integral")
                simgaCount += 1
                print(simgaCount)
            elif (graph[config[0]][config[len(config) - 1]] == 1 and graph[config[0]][config[len(config) - 1]] == 1):
                print("2 and 1 not connected")
        for adjacencyArray in graph:
            arrayOfGraphs.append(adjacencyArray)
            # print(adjacencyArray)
            # print(adjacencyArray[0])
            # if(adjacencyArray[3][2] == 1):
            #     print("Edge between 3 and 2")
            # else:
            #     print("no edge between 3 and 2")

    print(f"Number of sinma integrals is: {simgaCount}")


def main():
    # printAllBiconnectedGraphs()
    # arrayOfGraphs[0]
    # Using normal lists
    biconnected_graphs = generate_biconnected_graphs_4_vertices()
    config = [1, 4, 3, 2]
    for graph in biconnected_graphs:
        # //insert first row and integers
        graph.insert(0, [0] + list(range(1, 5)))
        for i in range(1, 5):
            # inserts first columns and integers
            graph[i].insert(0, i)

    for i, graph in enumerate(biconnected_graphs):
        print(f'Graph {i + 1}')
        for row in graph:
            print(row)
    # for(k) in range(len(graph)):
    #     for j in range(len(graph[k])):
    #         element = graph[k][j]
    #         if(graph[config[0][config[4]]] == 1):
    #             print(f"Sigma integral: {config}")
    #         # print(element)

    # print(adjacency_matrices)
    # printBiconnected()


main()
