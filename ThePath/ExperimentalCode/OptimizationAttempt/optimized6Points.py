import sympy as sp
import math
from itertools import permutations, zip_longest
import time

limit = 1
limitsArray = []
index = 0
limitIndex = 0
indexOuter = 0
indexOuterTwo = 0
integralValue = 0
duplicateLimitsArray = []



def countIntegralFrequency():
    valueArray = assignValueToUniqueIntegrals()
    # print(f"valueArrayZ: {valueArray}")
    uniqueLimits = getUniqueLimits()
    # print(f"UniqueLimitsZ: {uniqueLimits}")
    valueDict = makeUniqueValueDict()
    # print(f"valueDictInCount: {valueDict}")
    countDict = {}
    for value in valueArray:
        if value in countDict:
            countDict[value] += 1
        else:
            countDict[value] = 1
    print(f"Count is: {countDict}")
    result = 0
    for key, value in countDict.items():
        result += (key*value)
    print(f"FinalValue: {result}")




def assignValueToUniqueIntegrals():
    uniqueLimitsIntegralValueDict = makeUniqueValueDict()
    print(f"Dictionary iz: {uniqueLimitsIntegralValueDict}")
    groupedLimitArray = getGroupedArray()
    totalIntegralValue = 0
    # print(f"groupedLimitArrayIZ: {groupedLimitArray}")
    timesArray = []
    for ALimit in groupedLimitArray:
        ALimit = tuple(map(tuple, ALimit))
        # print(ALimit)
        if ALimit in uniqueLimitsIntegralValueDict:
            # print(ALimit)
            # add count of each integral.
            # scale the number of points to others, and reproducde B4 and B5.
            valueOfIntegral = uniqueLimitsIntegralValueDict[ALimit]
            # print(valueOfIntegral)
            # totalIntegralValue += valueOfIntegral
            timesArray.append(valueOfIntegral)
    # print(f"TotalIntegralValueIz: {totalIntegralValue}")
    # print(f"timesArray: {timesArray}")
    return timesArray



def makeUniqueValueDict():
    varList = [0, sp.Symbol('w'), sp.Symbol('x'), sp.Symbol('y'), sp.Symbol('z'), sp.Symbol('a')]
    uniqueLimitsWithValue = insertUniqueIntegralValue()
    uniqueLimitsIntegralValueDict = {}
    for uniqueLimit in uniqueLimitsWithValue:
        key = tuple(tuple(i) for i in uniqueLimit[:4])
        value = uniqueLimit[-1]
        uniqueLimitsIntegralValueDict[key] = value
    uniqueLimitsIntegralValueDictTuple = {tuple(key): value for key, value in uniqueLimitsIntegralValueDict.items()}
    print(f"uniqueLimitsIntegralValueDictTuple: {uniqueLimitsIntegralValueDictTuple}")
    return uniqueLimitsIntegralValueDictTuple



def insertUniqueIntegralValue():
    uniqueIntegralsValue = calcUniqueIntegrals()
    uniqueLimits = getUniqueLimits()
    for i in range(len(uniqueLimits)):
        uniqueLimits[i].append(uniqueIntegralsValue[i])
    # print(f"uniqueLimitsWithIntegralValue: {uniqueLimits}")
    return uniqueLimits


def calcUniqueIntegrals():
    global indexOuterTwo
    valueUniqueIntegrals = []
    uniqueLimits = getUniqueLimits()
    # uniqueArray is: [[[a, 1], [z, 1], [y, 1], [x, 1]], [[a, y + 1], [z, 1], [y, 1], [x, 1]],
    #                  [[a, x + 1], [z, 1], [y, 1], [x, 1]], [[a, y + 1], [z, x + 1], [y, 1], [x, 1]],
    #                  [[a, x + 1], [z, x + 1], [y, 1], [x, 1]], [[a, w + 1], [z, 1], [y, 1], [x, 1]],
    #                  [[a, x + 1], [z, w + 1], [y, 1], [x, 1]], [[a, w + 1], [z, w + 1], [y, 1], [x, 1]],
    #                  [[a, x + 1], [z, x + 1], [y, w + 1], [x, 1]], [[a, y + 1], [z, x + 1], [y, w + 1], [x, 1]],
    #                  [[a, x + 1], [z, w + 1], [y, w + 1], [x, 1]], [[a, w + 1], [z, w + 1], [y, w + 1], [x, 1]],
    #                  [[a, y + 1], [z, w + 1], [y, w + 1], [x, 1]], [[a, y + 1], [z, w + 1], [y, 1], [x, 1]]]
    varList = [0, sp.Symbol('w'), sp.Symbol('x'), sp.Symbol('y'), sp.Symbol('z'), sp.Symbol('a')]
    toBeIntegrated = (varList[-1]) ** 0
    # for uniqueLimit in uniqueLimits:
    #     for limitIndex in range(4):
    #
    #         print(f"indexOuteris: {indexOuterTwo}")
    #         result = sp.integrate(toBeIntegrated, (varList[-limitIndex - 1], (varList[-limitIndex - 2], uniqueLimit[limitIndex][1])))
    #         # print(
    #             # f"(toBeIntegrated, varList[-indexLimits - 1], (varList[-indexLimits - 2], uniqueLimits[indexOuterTwo][indexOuterTwo][1])):{(toBeIntegrated, varList[-limitIndex - 1], (varList[-limitIndex - 2], uniqueLimits[indexOuterTwo][indexOuterTwo][1]))}")
    #         toBeIntegrated = result
    #         indexOuterTwo += 1
    #         print(f"result is: {result}")
    #     result = sp.integrate(toBeIntegrated, (varList[1], (0, 1)))
    #     print(f"result is: {result}")
    for j in range(len(uniqueLimits)):
        for i in range(len(uniqueLimits[0])-1):
            if(i < len(uniqueLimits)):
                # print(f"i is: {i}")
                result = sp.integrate(toBeIntegrated, (uniqueLimits[j][i][0], (uniqueLimits[j][1+i][0],
                                                                               uniqueLimits[j][i][1])))
                # result = sp.integrate
                # print(f"toBeIntegrated, (uniqueLimits[j][i][0], (uniqueLimits[j][1+i][0],uniqueLimits[j][i][1])): {toBeIntegrated, (uniqueLimits[j][i][0], (uniqueLimits[j][1+i][0],uniqueLimits[j][i][1]))}")
                # print(result)
                toBeIntegrated = result
        # print(f"toBeIntegrated, (varList[1], (0, 1)): {toBeIntegrated, (varList[2], (varList[1], 1))}")
        result = sp.integrate(toBeIntegrated, (varList[2], (varList[1], 1)))
        toBeIntegrated = result
        # print(f"toBeIntegrated, (varList[1], (0, 1)): {toBeIntegrated, (varList[1], (0, 1))}")
        result = sp.integrate(toBeIntegrated, (varList[1], (0, 1)))
        # print(f"lastLt: {uniqueLimits[0]}")
        toBeIntegrated = (varList[-1]) ** 0
        valueUniqueIntegrals.append(result)
        # print(f"finalIntegral: {result}")
    # print(f"valueUniqueIntegrals:{valueUniqueIntegrals}")
    return valueUniqueIntegrals



def calcIntegral(varList):
    global limitIndex
    global indexOuter
    global integralValue
    # TODO: It is not necessary to calculate all the integrals. Figure out a way to calculate just all the unique
    #  integrals and then use their values when ver need be.
    for limitIndex in range(len(varList) - 2):
        duplicateLimitsArray.append([varList[-limitIndex - 1], limitsArray[indexOuter][1]])
        indexOuter += 1


def getAdjacencyMatrix():
    adjacencyMatrix = [
            [0, 1, 2, 3, 4, 5, 6],
            [1, 0, 1, 0, 0, 0, 1],
            [2, 1, 0, 1, 0, 0, 0],
            [3, 0, 1, 0, 1, 0, 0],
            [4, 0, 0, 1, 0, 1, 0],
            [5, 0, 0, 0, 1, 0, 1],
            [6, 1, 0, 0, 0, 1, 0]
        ]
    return adjacencyMatrix



def getAllPermutations(anyPermutation):
    perms = list(permutations(anyPermutation))
    allPermutations = []
    for perm in perms:
        allPermutations.append(perm)
    return allPermutations



def getVarList():
    varList = [0, sp.Symbol('w'), sp.Symbol('x'), sp.Symbol('y'), sp.Symbol('z'), sp.Symbol('a')]
    return varList


def printOneLimit(primaryNode, permutation, overlapTracker, adjacencyMatrix, varList):
    global index
    global limit
    # secondaryNode: leftmost point, varied until a connection with fixed rightmost point is found.
    for secondaryNode in range(len(permutation) - 1):
        # Start of contribution by Shaykh Umar; stop checking for connections beyond the rightmost fixed point
        if (permutation[-primaryNode - 1] == permutation[secondaryNode]):
            break
        # End of contribution by Shaykh Umar if position primaryNode and secondary node are connected and connection
        # is not overlapped, then upperLimit of primary node position is the position it is connected to,
        # which is secondaryNode.
        if (adjacencyMatrix[permutation[-primaryNode - 1]][permutation[secondaryNode]] and
                (not overlapTracker[secondaryNode])):
            # print(f"UpperLimit integration variable in if   {varList[-primaryNode - 1]} "
            #       f" : {1 + varList[secondaryNode]} ")
            limit = 1 + varList[secondaryNode]
            limitsArray.append(([varList[-primaryNode - 1], limit]))
            for i in range(secondaryNode, (len(permutation) - primaryNode)):
                # keeps track of overlapping connections and helps ignore limits generated by overlapping points
                overlapTracker[i] = 1
            break
        # if the connection between primary and secondary nodes is overlapping then the limit of primary node will
        # be the limit of rightMost limit. This limit is the same as limit calculated in last calculation, that's why we
        # need to use global variables, so that we can access the limit in "if" as well as "else-if" conditional.
        elif (overlapTracker[secondaryNode] == 1 and overlapTracker[-primaryNode - 1] == 1):
            # to assign the limit of rightMost limit
            # print(f"UpperLimit integration variable in elif {varList[-primaryNode - 1]}  : {limit}")
            limitsArray.append(([varList[-primaryNode - 1], limit]))
            # as soon an overlapping connection is found, conditional breaks because all the connections
            # beyond(to the right) of that position will necessarily be overlapping.
            break


def printAllLimit(permutation, overlapTracker, varList, adjacencyMatrix):
    # primaryNode: rightMost point, fixed to check connections secondary node
    for primaryNode in range(math.floor((len(permutation) - 1) / 2) + 2):
        printOneLimit(primaryNode, permutation, overlapTracker, adjacencyMatrix, varList)
    sumAllIntegrals = calcIntegral(varList)
    return sumAllIntegrals


def getGroupedArray():
    groupedList = list(zip_longest(*[iter(limitsArray)] * 4))
    groupedArray = []
    for subArray in groupedList:
        groupedArray.append(subArray)
    # print(f"groupedArray is: {groupedArray}")
    return groupedArray




def getUniqueLimits():
    grouped_list = list(zip_longest(*[iter(duplicateLimitsArray)] * 4))
    uniqueArray = []
    for sub_array in grouped_list:
        sub_array = list(sub_array)
        if sub_array not in uniqueArray:
            uniqueArray.append(sub_array)
    # print(f"uniqueArray is: {uniqueArray}")
    # print(f"LenUniqueArray is: {len(uniqueArray)}")
    return uniqueArray








def main():
    start_time = time.time()
    adjacencyMatrix = getAdjacencyMatrix()
    anyPermutation = [1, 2, 3, 4, 5, 6]
    # gets an array with all possible permutations of parameter permutations
    permutations = getAllPermutations(anyPermutation)
    # gets the variable list
    varList = getVarList()
    # Sum of all the integrals for cyclic-biconnected graph of 6 points
    sumAllIntegrals = 0
    for indexPermutation in range(len(permutations)):
        overlapTracker = [0] * (len(anyPermutation))
        # print(f"Integral Number: {indexPermutation + 1}: {permutations[indexPermutation]}")
        # overlapTracker: global variable
        sumAllIntegrals = printAllLimit(permutations[indexPermutation], overlapTracker, varList, adjacencyMatrix)
        # print()
    # getGroupedArray()
    # getUniqueLimits()
    # calcUniqueIntegrals()
    # insertUniqueIntegralValue()
    # makeUniqueValueDict()
    # assignValueToUniqueIntegrals()
    countIntegralFrequency()
    # print(f"Sum of values of all given integrals is : {sumAllIntegrals}")
    print("--- %s seconds ---" % (time.time() - start_time))


# test report Notes: Don't check for connections for if primary is less than secondary, i.e. it should not check if 4
# is connected to 5, it wil have already check that 5 is connected to 4, only check for left side, i.e. higher index
# should check for connection with lower index nodes not the other way around


main()
