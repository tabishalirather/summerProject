import numpy as np
import sympy as sp
import math
limit = 1
limitsArray = []
index = 0


def getAdjacencyMatrix():
    adjacencyMatrix = np.array(
        [
            [0, 1, 2, 3, 4, 5],
            [1, 0, 1, 0, 0, 1],
            [2, 1, 0, 1, 0, 0],
            [3, 0, 1, 0, 1, 0],
            [4, 0, 0, 1, 0, 1],
            [5, 1, 0, 0, 1, 0]
        ])
    return adjacencyMatrix


def getPermutation():
    # combination = [[1, 2, 4, 5, 3], [1, 2, 5, 4, 3], [1, 5, 2, 4, 3], [1, 5, 4, 2, 3], [1, 4, 2, 5, 3],
    #                [1, 4, 5, 2, 3]]
    # combination = [[2, 1, 3, 5, 4], [2, 1, 5, 3, 4], [2, 3, 1, 5, 4], [2, 3, 5, 1, 4], [2, 5, 1, 3, 4],
    #                [2, 5, 3, 1, 4]]
    combination = [[2, 1, 3, 4, 5], [2, 1, 4, 3, 5], [2, 3, 1, 4, 5], [2, 3, 4, 1, 5], [2, 4, 1, 3, 5],
                   [2, 5, 3, 1, 4]]

    return combination


def getVarList():
    varList = [0, sp.Symbol('w'), sp.Symbol('x'), sp.Symbol('y'), sp.Symbol('z')]
    return varList


def printOneLimit(primaryPoint, permutation, overlapTracker):
    adjacencyMatrix = getAdjacencyMatrix()
    varList = getVarList()
    global index
    # rightMostLimit = varList[0]
    global limit
    for secondaryNode in range(len(permutation) - 1):
        # Start of contribution by Shaykh Umar
        if (permutation[-primaryPoint - 1] == permutation[secondaryNode]):
            break
        #     End of contribution by Shaykh Umar
        if (adjacencyMatrix[permutation[-primaryPoint - 1]][permutation[secondaryNode]] and
                (not overlapTracker[secondaryNode])):
            # (len(permutation) - primaryPoint != secondaryNode+2) and over):
            # (adjacencyMatrix[permutation[-primaryPoint - 2]][permutation[secondaryNode+1]])):
            # print(f"Value blocker: {overlapTracker[secondaryNode]}")
            # print(f"overlapTracker: {overlapTracker}")
            # print(f"Permutation: {permutation}")
            # print(f"Secondary Node: {secondaryNode}")
            # print(
            #     f"{permutation[-primaryPoint - 1]} at position {len(permutation) - primaryPoint} is connected to "
            #     f"{permutation[secondaryNode]} at position {secondaryNode + 1}")
            print(f"UpperLimit integration variable in if   {varList[-primaryPoint - 1]} "
                  f" : {1 + varList[secondaryNode]} ")
            limit = 1 + varList[secondaryNode]
            # print(f"limit = {limit}")
            limitsArray.append(([varList[-primaryPoint - 1], limit]))
            print(f"limit = {limitsArray}")
            for i in range(secondaryNode, (len(permutation) - primaryPoint - 1) + 1):
                overlapTracker[i] = 1
            break
        elif (overlapTracker[secondaryNode] == 1 and overlapTracker[-primaryPoint - 1] == 1):
            # print("Running in elif") print( f"overlap: {permutation[-primaryPoint - 1]} has overlapping connection
            # with {permutation[secondaryNode]} at " f"position {secondaryNode + 1}")
            print(f"UpperLimit integration variable in elif {varList[-primaryPoint - 1]}  : {limit}")
            limitsArray.append(([varList[-primaryPoint - 1], limit]))
            print(f"limit = {limitsArray}")
            break
            # print(f"limitsArray are: {limitsArray}")
            # limitsArray.append(([varList[-primaryPoint - 1], limit]))

        # else: print("") # print( #     f"{permutation[-primaryPoint - 1]} at position {len(permutation) -
        # primaryPoint} is not connected to " #     f"{permutation[secondaryNode]} at position {secondaryNode + 1}")


def printAllLimit(permutation, overlapTracker):
    for primaryNode in range(math.floor((len(permutation) - 1) / 2) + 1):
        printOneLimit(primaryNode, permutation, overlapTracker)


def main():
    permutation = getPermutation()
    # print(permutation[1])
    for index in range(len(permutation)):
        overlapTracker = [0] * (len(permutation) - 1)
        print(f"Integral Number: {index + 1}: {permutation[index]}")
        printAllLimit(permutation[index], overlapTracker)
        print()


# test report Notes: Don't check for connections for if primary is less than secondary, i.e. it should not check if 4
# is connected to 5, it wil have already check that 5 is connected to 4, only check for left side, i.e. higher index
# should check for connection with lower index nodes not the other way around


main()
