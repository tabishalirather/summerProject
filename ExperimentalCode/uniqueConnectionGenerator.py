import numpy as np
import sympy as sp
import math


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


def getCombination():
    combination = [[1, 2, 4, 5, 3], [1, 2, 5, 4, 3], [1, 5, 2, 4, 3], [1, 5, 4, 2, 3], [1, 4, 2, 5, 3],
                   [1, 4, 5, 2, 3], ]
    return combination


def getVarList():
    varList = [0, sp.Symbol('w'), sp.Symbol('x'), sp.Symbol('y'), sp.Symbol('z')]
    return varList


def printOneLimit(primaryPoint, combination):
    adjacencyMatrix = getAdjacencyMatrix()
    varList = getVarList()
    for secondaryNode in range(len(combination) - 1):
        if (adjacencyMatrix[combination[-primaryPoint - 1]][combination[secondaryNode]]):
            print(
                f"{combination[-primaryPoint - 1]} is connected to  "
                f"{combination[secondaryNode]} at position {secondaryNode + 1}")
            print(f"UpperLimit of integration variable {varList[-primaryPoint - 1]}  "
                  f"will be {1 + varList[secondaryNode]} ")
            break
        else:
            print(
                f"{combination[-primaryPoint - 1]} is not connected to  {combination[secondaryNode]} at position {secondaryNode + 1}")


def printAllLimit(combination):
    for primaryNode in range(math.floor((len(combination) - 1) / 2) + 1):
        printOneLimit(primaryNode, combination)


def main():
    combinations = getCombination()
    print(combinations[1])
    for index in range(len(combinations)):
        print(f"Integral Number: {index + 1}: {combinations[index]}")
        printAllLimit(combinations[index])
        print()


# test report Notes: Don't check for connections for if primary is less than secondary, i.e is should not check if 4
# is connected to 5, it wil have already check that 5 is connected to 4, only check for left side, i.e higher index
# should check for connection with lower index nodes not the other way around



main()
