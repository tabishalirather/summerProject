import numpy as np
adjacencyMatrix = np.array([
                   [0, 1, 2, 3, 4],
                   [1, 0, 1, 0, 1],
                   [2, 1, 0, 1, 0],
                   [3, 0, 1, 0, 1],
                   [4, 1, 0, 1, 0]
                   ])
combination = [1, 4, 2, 3]
# print(adjacencyMatrix[1][1])
# print(adjacencyMatrix[1][2])
# print(adjacencyMatrix.shape[0]-1)
connectedNodes = []
for row in range(1, adjacencyMatrix.shape[0]):
    # column = row
    # for columnCount in range(rowCount, adjacencyMatrix.shape[1]):
    for column in range(1, adjacencyMatrix.shape[1]):
        # print(f"{rowCount}, {columnCount}")
        if((adjacencyMatrix[row][column]) == 1):
            # print(f"(a,b) {rowCount},{columnCount}")
            connectedNodes.append((row, column))
# print(connectedNodes)
#
# Create an empty set to store the unique nodes
unique_nodes = set()

# Iterate over the nodes in the list
for node in connectedNodes:
    # Add the node to the set, if it is not already present
    # The set will automatically remove any duplicates
    unique_nodes.add(tuple(sorted(node)))
# Convert the set back to a list
unique_nodes = list(unique_nodes)
# Print the unique nodesstupidwhy the
print(unique_nodes)

# for element in combination:
#     print(f"element is: {element}")
#     print(adjacencyMatrix[element])
#     # print((adjacencyMatrix[element][element]+1))
# if(adjacencyMatrix[combination[0]combination[1]]):
#     print(adjacencyMatrix[combination[0]combination[1]]):
#     # print(f"{combination[0] , combination[1]}")
# firstelement = combination[0]
# # print(firstelement)
# secondElement = combination[1]
# # print(secondElement)
# print(adjacencyMatrix[firstelement][secondElement])
# print(adjacencyMatrix[combination[0]][combination[1]])
furthestConnected = []
finalFurthest = []
previousIndex = 0
count = 0
for element in range(1, adjacencyMatrix.shape[0] - 1):
    if(adjacencyMatrix[combination[0]][combination[element]] == 1):
        print(f"Index 0 Connected to: {element}")
        # print(((combination[0]), (combination[element])))
        furthestConnected.append([(combination[0], combination[element])])
        count += 1
else:
    finalFurthest.append(furthestConnected[-1])

for element in range(2, adjacencyMatrix.shape[0] - 1):
    if (adjacencyMatrix[combination[1]][combination[element]] == 1):
        print(f"Index 1 Connected to: {element}")
        print(((combination[1]), (combination[element])))
        furthestConnected.append([(combination[1], combination[element])])
        # finalFurthest.append(furthestConnected[-1])
        print(f"count is: {count}")
else:
    finalFurthest.append(furthestConnected[-1])

#
for element in range(3, adjacencyMatrix.shape[0] - 1):
    if (adjacencyMatrix[combination[2]][combination[element]] == 1):
        print(f"Index 2 Connected to: {element}")
        print(((combination[2]), (combination[element])))
        print(combination)
        furthestConnected.append([(combination[2], combination[element])])
else:
    finalFurthest.append(furthestConnected[-1])

print(finalFurthest)






