import sympy as sp
import math
from itertools import permutations, zip_longest
import time

limit = 0
limitsArray = []
index = 0
limitIndex = 0
indexOuter = 0
integralValue = 0
timeCalcIntegral = 0
duplicateLimitsArray = []


def countIntegralFrequency():
    valueArray = assignValueToUniqueIntegrals()
    print(f"valueArrayZ: {valueArray}")
    uniqueLimits = getUniqueLimits()
    print(f"UniqueLimitsZ: {uniqueLimits}")
    valueDict = makeUniqueValueDict()
    print(f"valueDictInCount: {valueDict}")
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
    print(f"groupedLimitArray: {groupedLimitArray}")
    timesArray = []
    for ALimit in groupedLimitArray:
        ALimit = tuple(map(tuple, ALimit))
        if ALimit in uniqueLimitsIntegralValueDict:
            # add count of each integral.
            # scale the number of points to others, and reproducde B4 and B5.
            valueOfIntegral = uniqueLimitsIntegralValueDict[ALimit]
            # print(valueOfIntegral)
            totalIntegralValue += valueOfIntegral
            timesArray.append(valueOfIntegral)
    print(f"TotalIntegralValueIz: {totalIntegralValue}")
    print(f"timesArray: {timesArray}")
    return timesArray


def makeUniqueValueDict():
    varList = [0, sp.Symbol('w'), sp.Symbol('x'), sp.Symbol('y')]
    uniqueLimitsWithValue = insertUniqueIntegralValue()
    uniqueLimitsIntegralValueDict = {}
    for uniqueLimit in uniqueLimitsWithValue:
        key = tuple(tuple(i) for i in uniqueLimit[:3])
        value = uniqueLimit[-1]
        uniqueLimitsIntegralValueDict[key] = value
    uniqueLimitsIntegralValueDictTuple = {tuple(key): value for key, value in uniqueLimitsIntegralValueDict.items()}
    return uniqueLimitsIntegralValueDictTuple


def insertUniqueIntegralValue():
    uniqueIntegralsValue = calcUniqueIntegrals()
    uniqueLimits = getUniqueLimits()
    for i in range(len(uniqueLimits)):
        uniqueLimits[i].append(uniqueIntegralsValue[i])
    print(f"uniqueLimitsWithIntegralValue: {uniqueLimits}")
    return uniqueLimits


def calcUniqueIntegrals():
    valueUniqueIntegrals = []
    uniqueLimits = getUniqueLimits()
    varList = [0, sp.Symbol('w'), sp.Symbol('x'), sp.Symbol('y')]
    toBeIntegrated = (varList[-1]) ** 0
    for j in range(len(uniqueLimits)):
        for i in range(len(uniqueLimits)):
            if(i < len(uniqueLimits)):
                result = sp.integrate(toBeIntegrated, (uniqueLimits[j][i][0], (uniqueLimits[j][1+i][0],
                                                                               uniqueLimits[j][i][1])))
                toBeIntegrated = result
        result = sp.integrate(toBeIntegrated, (uniqueLimits[0][2][0], (0, 1)))
        valueUniqueIntegrals.append(result)
        toBeIntegrated = (varList[-1]) ** 0
    return valueUniqueIntegrals



def calcIntegral(varList):
    global limitIndex
    global indexOuter
    global integralValue
    varList = [0, sp.Symbol('w'), sp.Symbol('x'), sp.Symbol('y')]
    for indexLimits in range(3):
        duplicateLimitsArray.append([varList[-indexLimits - 1], limitsArray[indexOuter][1]])
        indexOuter += 1
    return integralValue


def getGroupedArray():
    groupedList = list(zip_longest(*[iter(limitsArray)] * 3))
    groupedArray = []
    for subArray in groupedList:
        groupedArray.append(subArray)
    return groupedArray


def getAllPermutations(anyPermutation):
    perms = list(permutations(anyPermutation))
    allPermutations = []
    for perm in perms:
        allPermutations.append(perm)
    return allPermutations



def getAdjacencyMatrix():
    adjacencyMatrix = [
        [0, 1, 2, 3, 4],
        [1, 0, 1, 0, 1],
        [2, 1, 0, 1, 0],
        [3, 0, 1, 0, 1],
        [4, 1, 0, 1, 0],
    ]
    return adjacencyMatrix


def getVarList():
    varList = [0, sp.Symbol('w'), sp.Symbol('x'), sp.Symbol('y')]
    return varList


def dealsWithOverlapping(primaryPoint, varList):
    print(f"UpperLimit integration variable in elif {varList[-primaryPoint - 1]}  : {limit}")
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
            print(f"UpperLimit integration variable in if   {varList[-primaryPoint - 1]} "
                  f" : {1 + varList[secondaryNode]} ")
            limit = 1 + varList[secondaryNode]
            limitsArray.append(([varList[-primaryPoint - 1], limit]))
            # Should I do -1 or not?
            for i in range(secondaryNode, (len(permutation) - primaryPoint - 1)):
                overlapTracker[i] = 1
            break
        elif (overlapTracker[secondaryNode] == 1 and overlapTracker[-primaryPoint - 1] == 1):
            dealsWithOverlapping(primaryPoint, varList)
            break


def printAllLimit(permutation, overlapTracker, varList, groupedArray):
    global timeCalcIntegral
    for primaryNode in range(math.floor((len(permutation) - 1) / 2) + 2):
        printOneLimit(primaryNode, permutation, overlapTracker, varList)
    valueFirstBiconnected = calcIntegral(varList)
    return valueFirstBiconnected


def getUniqueLimits():
    grouped_list = list(zip_longest(*[iter(duplicateLimitsArray)] * 3))
    uniqueArray = []
    for sub_array in grouped_list:
        sub_array = list(sub_array)
        if sub_array not in uniqueArray:
            uniqueArray.append(sub_array)
    return uniqueArray


def main():
    start_time = time.time()
    anyPermutation = [1, 2, 3, 4]
    # Using permutations from below line of code generates 5! = 120 cases
    permutation = getAllPermutations(anyPermutation)
    valueFirstBiconnected = 0
    global index
    varList = getVarList()
    start_all_print = time.time()
    groupedArray = getGroupedArray()
    for indexPermutation in range(len(permutation)):
        overlapTracker = [0] * (len(anyPermutation) - 1)
        print(f"Integral Number: {indexPermutation + 1}: {permutation[indexPermutation]}")
        valueFirstBiconnected = printAllLimit(permutation[indexPermutation], overlapTracker, varList, groupedArray)
        print()
    uniqueArray = getUniqueLimits()
    groupedArray = getGroupedArray()
    print(f"UniqueLimits: {uniqueArray}")
    end_all_print = time.time()
    assignValueToUniqueIntegrals()
    countIntegralFrequency()
    exec_time = -start_all_print + end_all_print
    print("--- %s seconds ---" % (time.time() - start_time))


# test report Notes: Don't check for connections for if primary is less than secondary, i.e. it should not check if 4
# is connected to 5, it wil have already check that 5 is connected to 4, only check for left side, i.e. higher index
# should check for connection with lower index nodes not the other way around


main()
