import numpy as np
import sympy as sp
import math
from itertools import permutations
import time

limit = 1
limitsArray = []
index = 0
indexLimits = 0
indexOuter = 0
integralValue = 0


def calcIntegral(varList):
    global indexLimits
    global indexOuter
    global integralValue

    # print(limitsArray)
    toBeIntegrated = varList[0] ** 0
    varList = [0, sp.Symbol('w'), sp.Symbol('x'), sp.Symbol('y'), sp.Symbol('z'), sp.Symbol('a'), sp.Symbol('b')]
    # Notes for tomorrow: Objective: need to evaluate integral for four limits and then update to
    for indexLimits in range(len(varList) - 2):
        # print(f"Index: {indexLimits}")
        # print(f"Second Index: {indexLimits}")
        # print(f"Outer index: {indexOuter}")
        result = sp.integrate(toBeIntegrated, (varList[-indexLimits - 1], (varList[-indexLimits - 2],
                                                                           limitsArray[indexOuter][1])))
        toBeIntegrated = result
        # print(f"Outer index is: {indexOuter}")
    # elif(indexOuter % 4):
    #     print(f"Outer index is: {indexOuter}")
        indexOuter += 1


        # print(f"(IntegrationVariable; lowerLimit; "
        #       f"UpperLimit {varList[-indexLimits - 1], (varList[-indexLimits - 2], limitsArray[indexOuter][1])}")
    # print(integralValue)
    result = sp.integrate(toBeIntegrated, (varList[1], (0, 1)))
    print(f"Value of Integral is: {result}")
    integralValue += result
    return integralValue


def getAdjacencyMatrix():
    adjacencyMatrix = np.array(
        [
            # [0, 1, 2, 3, 4, 5],
            # [1, 0, 1, 0, 0, 1],
            # [2, 1, 0, 1, 0, 0],
            # [3, 0, 1, 0, 1, 0],
            # [4, 0, 0, 1, 0, 1],
            # [5, 1, 0, 0, 1, 0]
            # [0, 1, 2, 3, 4, 5, 6],
            # [1, 0, 1, 0, 0, 0, 1],
            # [2, 1, 0, 1, 0, 0, 0],
            # [3, 0, 1, 0, 1, 0, 0],
            # [4, 0, 0, 1, 0, 1, 0],
            # [5, 0, 0, 0, 1, 0, 1],
            # [6, 1, 0, 0, 0, 1, 0]
            # 7 Points

            [0, 1, 2, 3, 4, 5, 6, 7],
            [1, 0, 1, 0, 0, 0, 0, 1],
            [2, 1, 0, 1, 0, 0, 0, 0],
            [3, 0, 1, 0, 1, 0, 0, 0],
            [4, 0, 0, 1, 0, 1, 0, 0],
            [5, 0, 0, 0, 1, 0, 1, 0],
            [6, 0, 0, 0, 0, 1, 0, 1],
            [7, 1, 0, 0, 0, 1, 0, 0]
        ])
    return adjacencyMatrix


# def getPermutation():
#     # combination = [[1, 2, 4, 5, 3], [1, 2, 5, 4, 3], [1, 5, 2, 4, 3], [1, 5, 4, 2, 3], [1, 4, 2, 5, 3],
#     #                [1, 4, 5, 2, 3]]
#     # combination = [[2, 1, 3, 5, 4], [2, 1, 5, 3, 4], [2, 3, 1, 5, 4], [2, 3, 5, 1, 4], [2, 5, 1, 3, 4],
#     #                [2, 5, 3, 1, 4]]
#     combination = [[2, 1, 3, 4, 5], [2, 1, 4, 3, 5], [2, 3, 1, 4, 5], [2, 3, 4, 1, 5], [2, 4, 1, 3, 5],
#                    [2, 5, 3, 1, 4]]
#     combination = [[2, 1, 3, 4, 5], [2, 1, 4, 3, 5], [2, 3, 1, 4, 5], [2, 3, 4, 1, 5], [2, 4, 1, 3, 5],
#                    [2, 5, 3, 1, 4]]
#     combination = permutations_with_fixed_elements()
#
#     return combination


def getAllPermutations(anyPermutation):
    perms = list(permutations(anyPermutation))
    allPermutations = []
    for perm in perms:
        allPermutations.append(perm)
    return allPermutations


# def permutations_with_fixed_elements():
#     arr = [1, 2, 4, 5, 6, 3]
#     perms = list(permutations(arr))
#     result = []
#     for perm in perms:
#         # print(perm)
#         result.append(perm)
#     return result


def getVarList():
    varList = [0, sp.Symbol('w'), sp.Symbol('x'), sp.Symbol('y'), sp.Symbol('z'), sp.Symbol('a'), sp.Symbol('b')]
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
            print(f"UpperLimit integration variable in if   {varList[-primaryPoint - 1]} "
                  f" : {1 + varList[secondaryNode]} ")
            limit = 1 + varList[secondaryNode]
            # print(f"limit = {limit}")
            limitsArray.append(([varList[-primaryPoint - 1], limit]))
            # print(f"limit = {limitsArray}")
            for i in range(secondaryNode, (len(permutation) - primaryPoint)):
                overlapTracker[i] = 1
            # print(overlapTracker)
            break

        elif (overlapTracker[secondaryNode] == 1 and overlapTracker[-primaryPoint - 1] == 1):
            # print("Running in elif") print( f"overlap: {permutation[-primaryNode - 1]} has overlapping connection
            # with {permutation[secondaryNode]} at " f"position {secondaryNode + 1}")
            print(f"UpperLimit integration variable in elif {varList[-primaryPoint - 1]}  : {limit}")
            limitsArray.append(([varList[-primaryPoint - 1], limit]))
            # print(f"limitsArray = {limitsArray}")
            break
            # print(f"limitsArray are: {limitsArray}")
            # limitsArray.append(([varList[-primaryNode - 1], limit]))

        # else: print("") # print( #     f"{permutation[-primaryNode - 1]} at position {len(permutation) -
        # primaryNode} is not connected to " #     f"{permutation[secondaryNode]} at position {secondaryNode + 1}")


def printAllLimit(permutation, overlapTracker, varList):
    for primaryNode in range(math.floor((len(permutation) - 1) / 2) + 2):
        printOneLimit(primaryNode, permutation, overlapTracker)
    valueFirstBiconnected = calcIntegral(varList)
    return valueFirstBiconnected


def main():
    start_time = time.time()
    anyPermutation = [1, 2, 3, 4, 5, 6, 7]
    permutation = getAllPermutations(anyPermutation)
    varList = getVarList()
    valueFirstBiconnected = 0
    print(permutation[0])
    for indexPermutation in range(len(permutation)):
        overlapTracker = [0] * (len(permutation[0]))
        print(f"Integral Number: {indexPermutation + 1}: {permutation[indexPermutation]}")
        valueFirstBiconnected = printAllLimit(permutation[indexPermutation], overlapTracker, varList)
        print()
    # print(f"limitsArray = {limitsArray}")
    # print(len(limitsArray))
    print(f"Sum of values of all given integrals is : {valueFirstBiconnected}")
    # new_array = [[sublist] for sublist in limitsArray]
    # arrayToBeReshaped = np.array(new_array)
    # arrayToBeReshaped = np.reshape(arrayToBeReshaped, (-1, 8))
    # print(arrayToBeReshaped)
    # print(new_array)
    print("--- %s seconds ---" % (time.time() - start_time))


# test report Notes: Don't check for connections for if primary is less than secondary, i.e. it should not check if 4
# is connected to 5, it wil have already check that 5 is connected to 4, only check for left side, i.e. higher index
# should check for connection with lower index nodes not the other way around


main()
