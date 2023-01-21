import numpy as np
import sympy as sp
import math
from itertools import permutations
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
    combination = [[2, 1, 3, 4, 5], [2, 1, 4, 3, 5], [2, 3, 1, 4, 5], [2, 3, 4, 1, 5], [2, 4, 1, 3, 5],
                   [2, 5, 3, 1, 4]]
    # combination = permutations_with_fixed_elements()

    return combination


def getVarList():
    varList = [0, sp.Symbol('w'), sp.Symbol('x'), sp.Symbol('y'), sp.Symbol('z')]
    return varList


def printOneLimit(primaryPoint, permutation, overlapTracker):
    adjacencyMatrix = getAdjacencyMatrix()
    varList = getVarList()
    global index
    global limit

    for secondaryNode in range(len(permutation) - 1):
        # Start of contribution by Shaykh Umar
        if (permutation[-primaryPoint - 1] == permutation[secondaryNode]):
            break
        #     End of contribution by Shaykh Umar
        if (adjacencyMatrix[permutation[-primaryPoint - 1]][permutation[secondaryNode]] and
                (not overlapTracker[secondaryNode])):
            print(f"UpperLimit integration variable in if   {varList[-primaryPoint - 1]} "
                  f" : {1 + varList[secondaryNode]} ")
            limit = 1 + varList[secondaryNode]
            limitsArray.append(([varList[-primaryPoint - 1], limit]))
            for i in range(secondaryNode, (len(permutation) - primaryPoint - 1) + 1):
                overlapTracker[i] = 1
            break
        elif (overlapTracker[secondaryNode] == 1 and overlapTracker[-primaryPoint - 1] == 1):
            print(f"UpperLimit integration variable in elif {varList[-primaryPoint - 1]}  : {limit}")
            limitsArray.append(([varList[-primaryPoint - 1], limit]))
            print(f"limit = {limitsArray}")
            break


def printAllLimit(permutation, overlapTracker):
    for primaryNode in range(math.floor((len(permutation) - 1) / 2) + 1):
        printOneLimit(primaryNode, permutation, overlapTracker)


def main():
    permutation = getPermutation()

    for indexPermutation in range(len(permutation)):
        overlapTracker = [0] * (len(permutation) - 1)
        print(f"Integral Number: {indexPermutation + 1}: {permutation[indexPermutation]}")
        printAllLimit(permutation[indexPermutation], overlapTracker)
        print()
        limitsArray.append("||")


# test report Notes: Don't check for connections for if primary is less than secondary, i.e. it should not check if 4
# is connected to 5, it wil have already check that 5 is connected to 4, only check for left side, i.e. higher index
# should check for connection with lower index nodes not the other way around


main()
