import numpy as np
import sympy as sp
import math
from itertools import permutations
import time
import timeit

limit = 1
limitsArray = []
index = 0
indexLimits = 0
indexOuter = 0
integralValue = 0
timeCalcIntegral = 0




def calcIntegral(varList):
    global indexLimits
    global indexOuter
    global integralValue
    # print("This is working")
    # print(limitsArray)
    toBeIntegrated = varList[0] ** 0
    varList = [0, sp.Symbol('w'), sp.Symbol('x'), sp.Symbol('y'), sp.Symbol('z')]
    # Notes for tomorrow: Objective: need to evaluate integral for four limits and then update to
    for indexLimits in range(4):
        # print(f"Index: {indexLimits}")
        # print(f"Second Index: {indexLimits}")
        # print(f"Outer index: {indexOuter}")
        result = sp.integrate(toBeIntegrated, (varList[-indexLimits - 1], (varList[-indexLimits - 2],
                                                                           limitsArray[indexOuter][1])))
        toBeIntegrated = result
        # print("Function called")
        # print(f"Outer index is: {indexOuter}")
        indexOuter += 1

        # print(f"(IntegrationVariable; lowerLimit; "
        #       f"UpperLimit {varList[-indexLimits - 1], (varList[-indexLimits - 2], limitsArray[indexOuter][1])}")
    print(f"Value of Integral is: {result}")
    integralValue += result
    # print(integralValue)
    return integralValue

    # result = sp.integrate(toBeIntegrated, (varList[-1], (varList[-1-1], limitsArray[0][1])))
    # print(f"(IntegrationVariable; lowerLimit; UpperLimt {varList[-1], (varList[-1-1], limitsArray[0][1])}")
    # print(f"Value of Integral is: {result}")
    # result = sp.integrate(result, (varList[-1-1], (varList[-1 - 1 - 1], limitsArray[0][1])))
    # print(f"(IntegrationVariable; lowerLimit; UpperLimt {varList[-1-1], (varList[-1 - 1 - 1], limitsArray[1][1])}")
    # print(f"Value of Integral is: {result}")
    # result = sp.integrate(result, (varList[-3], (varList[-1 - 1 - 1 - 1], limitsArray[2][1])))
    # print(f"(IntegrationVar; lowerLimit; UpperLimt {varList[-3], (varList[-1-1-1-1], limitsArray[2][1])}")
    # print(f"Value of Integral is: {result}")
    # result = sp.integrate(result, (varList[-4], (varList[-1 - 1 - 1 - 1 - 1], limitsArray[3][1])))
    # print(f"(IntegrationVar; lowerLimit; UpperLimt {varList[-4], (varList[-1 - 1 - 1 - 1 - 1], limitsArray[3][1])}")
    # print(f"Value of Integral is: {result}")
    # print(f"Index in calcIntegral is: {indexLimits}")
    # if(indexLimits < 4):
    #     result = sp.integrate(toBeIntegrated, (varList[-indexLimits - 1], varList[-indexLimits - 2], limitOfIntegral))
    #     print(f"Integral result is: {result}")
    #     print(
    #         f"(variableIntegration, lowerLimit, upperLimit): {(varList[-indexLimits - 1], varList[-indexLimits - 2], limitOfIntegral)}")
    #     indexLimits += 1
    # elif(indexLimits == 4):
    #     print(f"Index outside calcIntegral is: {indexLimits}")
    #     result = sp.integrate(toBeIntegrated, (varList[1], 0, 1))
    #     print(f"Result of first integral is: {result}")
    #     print(f"(variableIntegration, lowerLimit, upperLimit): {(varList[1], 0, 1)}")


def getAllPermutations(anyPermutation):
    perms = list(permutations(anyPermutation))
    allPermutations = []
    for perm in perms:
        allPermutations.append(perm)
    return allPermutations


def testConfigurations():
    testConfig = [[1, 2, 4, 5, 3], [1, 2, 5, 4, 3], [1, 5, 2, 4, 3], [1, 5, 4, 2, 3], [1, 4, 2, 5, 3], [1, 4, 5, 2, 3]]
    return testConfig


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


def getVarList():
    varList = [0, sp.Symbol('w'), sp.Symbol('x'), sp.Symbol('y'), sp.Symbol('z')]
    return varList


def dealsWithOverlapping(primaryPoint, permutation, overlapTracker, varList):
    # print(f"UpperLimit integration variable in elif {varList[-primaryNode - 1]}  : {limit}")
    limitsArray.append(([varList[-primaryPoint - 1], limit]))
    # print(f"limit = {limitsArray}")


# def findsLimitsAndTracksOverlap(primaryNode, permutation, overlapTracker, varList, secondaryNode, ad):
#     if(adjacencyMatrix[permutation[-primaryNode - 1]][permutation[secondaryNode]] and
#             (not overlapTracker[secondaryNode])):
#         # findsLimitsAndTracksOverlap(primaryNode, permutation, overlapTracker, varList, secondaryNode)
#         print(f"UpperLimit integration variable in if   {varList[-primaryNode - 1]} "
#               f" : {1 + varList[secondaryNode]} ")
#         limit = 1 + varList[secondaryNode]
#         limitsArray.append(([varList[-primaryNode - 1], limit]))
#         # Should I do -1 or not?
#         for i in range(secondaryNode, (len(permutation) - primaryNode - 1)):
#             overlapTracker[i] = 1
#         break
#     elif (overlapTracker[secondaryNode] == 1 and overlapTracker[-primaryNode - 1] == 1):
#         dealsWithOverlapping(primaryNode, permutation, overlapTracker, varList)
#         break


def printOneLimit(primaryPoint, permutation, overlapTracker, varList):
    adjacencyMatrix = getAdjacencyMatrix()
    global index
    global limit
    for secondaryNode in range(len(permutation) - 1):
        # Start of contribution by Shaykh Umar
        if (permutation[-primaryPoint - 1] == permutation[secondaryNode]):
            break
        #     End of contribution by Shaykh Umar
        if (adjacencyMatrix[permutation[-primaryPoint - 1]][permutation[secondaryNode]] and
                (not overlapTracker[secondaryNode])):
            # findsLimitsAndTracksOverlap(primaryNode, permutation, overlapTracker, varList, secondaryNode)
            # print(f"UpperLimit integration variable in if   {varList[-primaryNode - 1]} "
            #       f" : {1 + varList[secondaryNode]} ")
            limit = 1 + varList[secondaryNode]
            limitsArray.append(([varList[-primaryPoint - 1], limit]))
            # print(f"Limit is: {limit}")
            # calcIntegral(varList, limit)
            # firstIntegral = 0
            # Should I do -1 or not?
            for i in range(secondaryNode, (len(permutation) - primaryPoint - 1)):
                overlapTracker[i] = 1
            break
        elif (overlapTracker[secondaryNode] == 1 and overlapTracker[-primaryPoint - 1] == 1):
            dealsWithOverlapping(primaryPoint, permutation, overlapTracker, varList)
            # print(f"Limit is: {limit}")
            # calcIntegral(varList, limit)
            break


def printAllLimit(permutation, overlapTracker, varList):
    global timeCalcIntegral
    for primaryNode in range(math.floor((len(permutation) - 1) / 2) + 2):
        printOneLimit(primaryNode, permutation, overlapTracker, varList)
        # print(limitsArray)
    valueFirstBiconnected = calcIntegral(varList)
    return valueFirstBiconnected


def main():
    start_time = time.time()
    anyPermutation = [1, 2, 3, 4, 5]
    # Using permutations from below line of code generates 5! = 120 cases
    permutation = getAllPermutations(anyPermutation)
    valueFirstBiconnected = 0
    global index
    # permutation = testConfigurations()
    varList = getVarList()
    # count = 0
    start_all_print = time.time()
    for indexPermutation in range(len(permutation)):
        # index += 1
        overlapTracker = [0] * (len(permutation[0]) - 1)
        print(f"Integral Number: {indexPermutation + 1}: {permutation[indexPermutation]}")
        valueFirstBiconnected = printAllLimit(permutation[indexPermutation], overlapTracker, varList)
        # print(overlapTracker)
        print()
    # print(len(limitsArray))
    end_all_print = time.time()
    exec_time = -start_all_print + end_all_print

    # valueFirstBiconnectedGraph = calcIntegral(varList)
    print(f"Sum of values of all given integrals is : {valueFirstBiconnected}")
    print("--- %s seconds ---" % (time.time() - start_time))


    # execution_time = timeit.timeit('calcIntegral(varList)', setup='from __main__ import calcIntegral',
    #                            globals={'varList': varList}, number=1)
    # print('Time taken:', execution_time)





# test report Notes: Don't check for connections for if primary is less than secondary, i.e. it should not check if 4
# is connected to 5, it wil have already check that 5 is connected to 4, only check for left side, i.e. higher index
# should check for connection with lower index nodes not the other way around


main()
