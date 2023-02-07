def check_edges():
    mat1 = [
        [0, 1, 2, 3, 4],
        [1, 0, 1, 0, 1],
        [2, 1, 0, 1, 0],
        [3, 0, 1, 0, 1],
        [4, 1, 0, 1, 0]
    ]

    arr = [1,3,2,4]
    n = len(arr)
    # Create a dictionary to store the connections
    connections = {}
    mat = enumerate(mat1)
    for i in range(n):
        connections[arr[i]] = set()
        for j in range(n):
            if mat[i, j] == 1:
                connections[arr[i]].add(arr[j])
    print(connections)
    return connections
