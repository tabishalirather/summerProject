from itertools import combinations
import numpy as np


def generate_biconnected_graphs(number_of_vertices):
    # Initialize the list of adjacency matrices
    adj_mats = []

    # Generate all combinations of edges in the complete graph
    edges = combinations(range(number_of_vertices), 2)
    edges = list(edges)

    # Iterate over all edges
    for u, v in edges:
        # Create a complete graph with 5 vertices
        adj_mat = [[0 for _ in range(number_of_vertices)] for _ in range(number_of_vertices)]
        for i, j in edges:
            adj_mat[i][j] = 1
            adj_mat[j][i] = 1

        # Remove the edge (u, v)
        adj_mat[u][v] = 0
        adj_mat[v][u] = 0

        # Check if the graph is biconnected
        is_biconnected = True
        visited = [False] * number_of_vertices
        low = [0] * number_of_vertices
        disc = [0] * number_of_vertices
        timestamp = 0

        def dfs(v, parent):
            nonlocal is_biconnected, timestamp
            visited[v] = True
            disc[v] = low[v] = timestamp
            timestamp += 1
            children = 0
            for u in range(number_of_vertices):
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


# def printBiconnected():
#     biconnected_graphs = generate_biconnected_graphs_4_vertices()
#     for i, graph in enumerate(biconnected_graphs):
#         print(f'Graph {i + 1}')
#         for row in graph:
#             print(row)


def printAllBiconnectedGraphs(number_of_vertices, config):
    allConfigs = permute(config)
    biconnected_graphs = generate_biconnected_graphs(number_of_vertices)
    # Code block adds vertices as first row and column for identification purpose
    for graph in biconnected_graphs:
        # //insert first row and integers
        graph.insert(0, [0] + list(range(1, number_of_vertices+1)))
        for i in range(1, number_of_vertices+1):
            # inserts first columns and integers
            graph[i].insert(0, i)

    for i, graph in enumerate(biconnected_graphs):
        print(f'Graph {i + 1}')
        for row in graph:
            print(row)



def main():
    config = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    number_of_vertices = 9
    printAllBiconnectedGraphs(number_of_vertices, config)


main()
