import sympy as sp
import math
from itertools import permutations, zip_longest
import time

limit = 1
limitsArray = []
index = 0
limitIndex = 0
indexOuter = 0
integralValue = 0
timeCalcIntegral = 0
duplicateLimitsArray = []



def countIntegralFrequency():
    valueArray = assignValueToUniqueIntegrals()
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
    print(f"LimitsAndValuesDict: {uniqueLimitsIntegralValueDict}")
    groupedLimitArray = getGroupedArray()
    timesArray = []
    for ALimit in groupedLimitArray:
        ALimit = tuple(map(tuple, ALimit))
        if ALimit in uniqueLimitsIntegralValueDict:
            # add count of each integral.
            # scale the number of points to others, and reproducde B4 and B5.
            valueOfIntegral = uniqueLimitsIntegralValueDict[ALimit]
            # print(valueOfIntegral)
            # totalIntegralValue += valueOfIntegral
            timesArray.append(valueOfIntegral)
    return timesArray


def makeUniqueValueDict():
    varList = [0, sp.Symbol('w'), sp.Symbol('x'), sp.Symbol('y'), sp.Symbol('z')]
    uniqueLimitsWithValue = insertUniqueIntegralValue()
    uniqueLimitsIntegralValueDict = {}
    for uniqueLimit in uniqueLimitsWithValue:
        key = tuple(tuple(i) for i in uniqueLimit[:len(uniqueLimitsWithValue) - 1])
        value = uniqueLimit[-1]
        uniqueLimitsIntegralValueDict[key] = value
    uniqueLimitsIntegralValueDictTuple = {tuple(key): value for key, value in uniqueLimitsIntegralValueDict.items()}
    # print(f"uniqueLimitsIntegralValueDictTuple: {uniqueLimitsIntegralValueDictTuple}")
    return uniqueLimitsIntegralValueDictTuple


def insertUniqueIntegralValue():
    uniqueIntegralsValue = calcUniqueIntegrals()
    uniqueLimits = getUniqueLimits()
    for i in range(len(uniqueLimits)):
        uniqueLimits[i].append(uniqueIntegralsValue[i])
    # print(f"uniqueLimitsWithIntegralValue: {uniqueLimits}")
    return uniqueLimits


def calcUniqueIntegrals():
    valueUniqueIntegrals = []
    uniqueLimits = getUniqueLimits()
    varList = [0, sp.Symbol('w'), sp.Symbol('x'), sp.Symbol('y'), sp.Symbol('z')]
    toBeIntegrated = (varList[-1]) ** 0
    for j in range(len(uniqueLimits)):
        for i in range(len(uniqueLimits) - 2):
            if(i < len(uniqueLimits)):
                result = sp.integrate(toBeIntegrated, (uniqueLimits[j][i][0], (uniqueLimits[j][1+i][0],
                                                                               uniqueLimits[j][i][1])))
                toBeIntegrated = result
        result = sp.integrate(toBeIntegrated, (uniqueLimits[0][len(uniqueLimits) - 2][0], (0, 1)))
        # print(uniqueLimits[0][len(uniqueLimits)-2][0])
        toBeIntegrated = (varList[-1]) ** 0
        # print(result)
        valueUniqueIntegrals.append(result)
    # print(f"valueUniqueIntegrals:{valueUniqueIntegrals}")
    return valueUniqueIntegrals


def calcIntegral(varList):
    global limitIndex
    global indexOuter
    global integralValue
    toBeIntegrated = varList[0] ** 0
    varList = [0, sp.Symbol('w'), sp.Symbol('x'), sp.Symbol('y'), sp.Symbol('z')]
    #  Notes for tomorrow: Objective: need to evaluate integral for four limits and then update to
    for indexLimits in range(4):
        duplicateLimitsArray.append([varList[-indexLimits - 1], limitsArray[indexOuter][1]])
        indexOuter += 1
    return integralValue



def getAllPermutations(anyPermutation):
    perms = list(permutations(anyPermutation))
    allPermutations = []
    for perm in perms:
        allPermutations.append(perm)
    return allPermutations



def getAdjacencyMatrix():
    # adjacencyMatrix = [
    #         [0, 1, 2, 3, 4, 5],
    #         [1, 0, 1, 0, 0, 1],
    #         [2, 1, 0, 1, 0, 0],
    #         [3, 0, 1, 0, 1, 0],
    #         [4, 0, 0, 1, 0, 1],
    #         [5, 1, 0, 0, 1, 0]
    #
    #     ]
    matrix = []
    with open(r"5Graph1Biconnected.txt", "r") as file:
        for line in file:
            matrix.append([int(x) for x in line.strip().split()])

    new_matrix = [[i + 1] + row for i, row in enumerate(matrix)]
    new_matrix.insert(0, [0, 1, 2, 3, 4, 5])
    # print(new_matrix)
    adjacencyMatrix = new_matrix
    return adjacencyMatrix


def getVarList():
    varList = [0, sp.Symbol('w'), sp.Symbol('x'), sp.Symbol('y'), sp.Symbol('z')]
    return varList


def dealsWithOverlapping(primaryPoint, varList):
    limitsArray.append(([varList[-primaryPoint - 1], limit]))


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
            limit = 1 + varList[secondaryNode]
            # varList = [0, sp.Symbol('w'), sp.Symbol('x'), sp.Symbol('y'), sp.Symbol('z')]
            limitsArray.append(([varList[-primaryPoint - 1], limit]))
            # Should I do -1 or not?
            for i in range(secondaryNode, (len(permutation) - primaryPoint - 1)):
                overlapTracker[i] = 1
            break
        elif (overlapTracker[secondaryNode] == 1 and overlapTracker[-primaryPoint - 1] == 1):
            dealsWithOverlapping(primaryPoint, varList)
            # print(f"Limit is: {limit}")
            # calcIntegral(varList, limit)
            break


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
    return uniqueArray


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
    permutation = getAllPermutations(anyPermutation)
    valueFirstBiconnected = 0
    global index
    varList = getVarList()
    start_all_print = time.time()
    for indexPermutation in range(len(permutation)):
        overlapTracker = [0] * (len(permutation[0]) - 1)
        valueFirstBiconnected = printAllLimit(permutation[indexPermutation], overlapTracker, varList)

    # assignValueToUniqueIntegrals()
    countIntegralFrequency()
    # getGroupedArray()
    end_all_print = time.time()
    exec_time = -start_all_print + end_all_print
    # print(f"Sum of values of all given integrals is : {valueFirstBiconnected}")
    print("--- %s seconds ---" % (time.time() - start_time))





# test report Notes: Don't check for connections for if primary is less than secondary, i.e. it should not check if 4
# is connected to 5, it wil have already check that 5 is connected to 4, only check for left side, i.e. higher index
# should check for connection with lower index nodes not the other way around


main()
