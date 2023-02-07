import sympy as sp
import math
from itertools import permutations, zip_longest
import time

limit = 1
limitsArray = []
indexOuter = 0
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
    groupedLimitArray = getGroupedArray()
    timesArray = []
    for ALimit in groupedLimitArray:
        ALimit = tuple(map(tuple, ALimit))
        if ALimit in uniqueLimitsIntegralValueDict:
            valueOfIntegral = uniqueLimitsIntegralValueDict[ALimit]
            timesArray.append(valueOfIntegral)
    return timesArray


def makeUniqueValueDict():
    uniqueLimitsWithValue = insertUniqueIntegralValue()
    uniqueLimitsIntegralValueDict = {}
    for uniqueLimit in uniqueLimitsWithValue:
        key = tuple(tuple(i) for i in uniqueLimit[:4])
        value = uniqueLimit[-1]
        uniqueLimitsIntegralValueDict[key] = value
    uniqueLimitsIntegralValueDictTuple = {tuple(key): value for key, value in uniqueLimitsIntegralValueDict.items()}
    print(f"limitAndValue: {uniqueLimitsIntegralValueDictTuple}")
    return uniqueLimitsIntegralValueDictTuple



def insertUniqueIntegralValue():
    uniqueIntegralsValue = calcUniqueIntegrals()
    uniqueLimits = getUniqueLimits()
    for i in range(len(uniqueLimits)):
        uniqueLimits[i].append(uniqueIntegralsValue[i])
    return uniqueLimits


def calcUniqueIntegrals():
    valueUniqueIntegrals = []
    uniqueLimits = getUniqueLimits()
    varList = [0, sp.Symbol('w'), sp.Symbol('x'), sp.Symbol('y'), sp.Symbol('z'), sp.Symbol('a')]
    toBeIntegrated = (varList[-1]) ** 0
    for j in range(len(uniqueLimits)):
        for i in range(len(uniqueLimits[0])-1):
            if(i < len(uniqueLimits)):
                result = sp.integrate(toBeIntegrated, (uniqueLimits[j][i][0], (uniqueLimits[j][1+i][0],
                                                                               uniqueLimits[j][i][1])))
                toBeIntegrated = result
        result = sp.integrate(toBeIntegrated, (varList[2], (varList[1], 1)))
        toBeIntegrated = result
        result = sp.integrate(toBeIntegrated, (varList[1], (0, 1)))
        toBeIntegrated = (varList[-1]) ** 0
        valueUniqueIntegrals.append(result)
    return valueUniqueIntegrals



def getGroupedArray():
    groupedList = list(zip_longest(*[iter(limitsArray)] * 4))
    groupedArray = []
    for subArray in groupedList:
        groupedArray.append(subArray)
    return groupedArray


def getUniqueLimits():
    grouped_list = list(zip_longest(*[iter(duplicateLimitsArray)] * 4))
    uniqueArray = []
    for sub_array in grouped_list:
        sub_array = list(sub_array)
        if sub_array not in uniqueArray:
            uniqueArray.append(sub_array)
    return uniqueArray


def makeDuplicateLimitsArray(varList):
    global indexOuter
    for indexLimits in range(len(varList) - 2):
        duplicateLimitsArray.append([varList[-indexLimits - 1], limitsArray[indexOuter][1]])
        indexOuter += 1


def getAdjacencyMatrix():
    matrix = []
    with open(r"6Graph1.txt", "r") as file:
        for line in file:
            matrix.append([int(x) for x in line.strip().split()])
    adjacencyMatrix = [[i + 1] + row for i, row in enumerate(matrix)]
    adjacencyMatrix.insert(0, [0, 1, 2, 3, 4, 5, 6])
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


def getOneLimit(primaryNode, permutation, overlapTracker, adjacencyMatrix, varList):
    global limit
    # secondaryNode: leftmost point, varied until a connection with fixed rightmost point is found.
    for secondaryNode in range(len(permutation) - 1):
        # Start of contribution by Shaykh Umar; stop checking for connections beyond the rightmost fixed point
        if (permutation[-primaryNode - 1] == permutation[secondaryNode]):
            break
        # End of contribution by Shaykh Umar
        # if position primaryNode and secondary node are connected and connection
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
            limitsArray.append(([varList[-primaryNode - 1], limit]))
            break


def getAllLimits(permutation, overlapTracker, varList, adjacencyMatrix):
    for primaryNode in range(math.floor((len(permutation) - 1) / 2) + 2):
        getOneLimit(primaryNode, permutation, overlapTracker, adjacencyMatrix, varList)
    makeDuplicateLimitsArray(varList)


def main():
    print("Hello mate! Working, Hold on!")
    start_time = time.time()
    adjacencyMatrix = getAdjacencyMatrix()
    anyPermutation = [1, 2, 3, 4, 5, 6]
    # gets an array with all possible permutations of parameter permutations
    permutation = getAllPermutations(anyPermutation)
    # gets the variable list
    varList = getVarList()
    for indexPermutation in range(len(permutation)):
        overlapTracker = [0] * (len(anyPermutation))
        getAllLimits(permutation[indexPermutation], overlapTracker, varList, adjacencyMatrix)
    countIntegralFrequency()
    print("--- %s seconds ---" % (time.time() - start_time))


main()
