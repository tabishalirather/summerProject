import sympy as sp


def permute(arr):
    from itertools import permutations
    # Generate all permutations of the list
    perms = list(permutations(arr))
    # print("All permutations")
    result = []
    for perm in perms:
        print(perm)
        result.append(perm)
    return result


def typeOfIntegralCount(adjacencyMatrix, anyParticularConfig):
    sigmaCount = 0
    wCount = 0
    wwCount = 0
    xCount = 0
    wxCount = 0
    allPerms = permute(anyParticularConfig)
    # perm will be an array, and perm[i] represents index i element in the array
    for perm in allPerms:
        # print(perm)
        # print(firstB4Connected[perm[0]][perm[len(perm)-1]])
        typeOfIntegralCountArray = []
        if (adjacencyMatrix[perm[0]][perm[len(perm) - 1]] == 1):
            print(f"Sigma integral: {perm}")
            sigmaCount += 1
        elif (adjacencyMatrix[perm[0]][perm[len(perm) - 2]] and adjacencyMatrix[perm[1]][perm[len(perm) - 1]] == 1):
            print(f"Omega  integral: {perm}")
            wCount += 1
        elif (adjacencyMatrix[perm[0]][perm[len(perm) - 3]] and adjacencyMatrix[perm[1]][perm[len(perm) - 1]] == 1):
            print(f"ww integral: {perm}")
            wwCount += 1
        elif (adjacencyMatrix[perm[0]][perm[len(perm) - 2]] and adjacencyMatrix[perm[2]][perm[len(perm) - 1]] == 1):
            print(f"x integral: {perm}")
            xCount += 1
        elif (adjacencyMatrix[perm[0]][perm[len(perm) - 3]] and adjacencyMatrix[perm[1]][perm[len(perm) - 2]] == 1 and
              adjacencyMatrix[perm[2]][perm[len(perm) - 1]] == 1):
            print(f"wx integral: {perm}")
            wxCount += 1

    # print(len(perm))
    print(f"No of sigma integrals is: {sigmaCount}")
    print(f"No of omega integrals is: {wCount}")
    print(f"No of ww integrals is: {wwCount}")
    print(f"No of x integrals is: {xCount}")
    print(f"No of wx integrals is: {wxCount}")
    print("\n")
    typeOfIntegralCountArray = [sigmaCount, wCount, wwCount, xCount, wxCount]
    return typeOfIntegralCountArray


def firstB5Biconnected():
    firstB5Graph = [
        [0, 1, 2, 3, 4, 5],
        [1, 0, 1, 0, 0, 1],
        [2, 1, 0, 1, 0, 0],
        [3, 0, 1, 0, 1, 0],
        [4, 0, 0, 1, 0, 1],
        [5, 1, 0, 0, 1, 0]
    ]
    return firstB5Graph





def secondB5Biconnected():
    secondB5Graph = [
        [0, 1, 2, 3, 4, 5],
        [1, 0, 1, 1, 0, 1],
        [2, 1, 0, 1, 1, 1],
        [3, 1, 1, 0, 1, 1],
        [4, 0, 1, 1, 0, 1],
        [5, 1, 1, 1, 1, 0],
    ]
    return secondB5Graph


def calcSigmaIntegral(varList):
    # f-dz, g-dy, x-dx, w-dw
    toBeIntegrated = varList[0] ** 0
    for i in (range(len(varList))):
        if (i != len(varList) - 1):
            result = sp.integrate(toBeIntegrated, (varList[i], varList[i + 1], 1))
            # print(f"Integral wrt d{varList[i]}: {result}")
            toBeIntegrated = result
        else:
            result = sp.integrate(toBeIntegrated, (varList[i], 0, 1))
            # print(f"{len(varList)}-Variable Sigma value is: {result}")
    return result


def calcOmegaIntegral(varList):
    # f-dz, g-dy, x-dx, w-dw
    toBeIntegrated = varList[0] ** 0
    isFirstIntegral = True
    for i in (range(len(varList))):
        if (i != len(varList) - 1):
            # check if integral is being calculated for first time and set limit accordingly
            if (isFirstIntegral):
                upperLimit = 1 + varList[len(varList) - 1]
                # integrate("function, Integration variable, lowLimit, Up-limit")
                result = sp.integrate(toBeIntegrated, (varList[i], varList[i + 1], upperLimit))
                # print(toBeIntegrated, (varList[i], varList[i + 1], upperLimit))
                print(f"Integral wrt d{varList[i]}: {result}")
                isFirstIntegral = False
            else:
                upperLimit = 1
                result = sp.integrate(toBeIntegrated, (varList[i], varList[i + 1], upperLimit))
                toBeIntegrated = result
                print(f"Integral wrt d{varList[i]}: {result}")
        else:
            # final integration with limits 0 to 1
            result = sp.integrate(toBeIntegrated, (varList[i], 0, 1))
            print(f"{len(varList)}-Variable Omega Integral value is: {result}")
    return result


def calcOmegaOmegaIntegral(varList):
    # f-dz, g-dy, x-dx, w-dw
    toBeIntegrated = varList[0] ** 0
    integralCount = 0
    upperLimit = 0
    for i in (range(len(varList))):
        if (i != len(varList) - 1):
            # upperLimit for first two integrations is omega and omega
            if (integralCount < 2):
                upperLimit = 1 + varList[-1]
                result = sp.integrate(toBeIntegrated, (varList[i], varList[i + 1], upperLimit))
                print(f"Integral wrt d{varList[i]}: {result}")
                toBeIntegrated = result
                integralCount += 1
            else:
                upperLimit = 1
                result = sp.integrate(toBeIntegrated, (varList[i], varList[i + 1], upperLimit))
                print(f"Integral wrt d{varList[i]}: {result}")
                toBeIntegrated = result
        else:
            result = sp.integrate(toBeIntegrated, (varList[i], 0, 1))
            print(f"{len(varList)}-Variable sigma value is: {result}")
    return result


def calcXIntegral(varList):
    # f-dz, g-dy, x-dx, w-dw
    toBeIntegrated = varList[0] ** 0
    isFirstIntegral = True
    for i in (range(len(varList))):
        if (i != len(varList) - 1):
            # check if integral is being calculated for first time and set limit accordingly
            if(isFirstIntegral):
                upperLimit = 1 + varList[len(varList) - 2]
                print(upperLimit)
                # integrate("function, Integration variable, lowLimit, Up-limit")
                result = sp.integrate(toBeIntegrated, (varList[i], varList[i + 1], upperLimit))
                print(toBeIntegrated, (varList[i], varList[i + 1], upperLimit))
                print(f"Integral wrt d{varList[i]}: {result}")
                isFirstIntegral = False
            else:
                upperLimit = 1
                result = sp.integrate(toBeIntegrated, (varList[i], varList[i + 1], upperLimit))
                toBeIntegrated = result
                print(f"Integral wrt d{varList[i]}: {result}")
        else:
            # final integration with limits 0 to 1
            result = sp.integrate(toBeIntegrated, (varList[i], 0, 1))
            print(f"{len(varList)}-Variable X Integral value is: {result}")
    return result


def calcOmegaXIntegral(varList):
    # f-dz, g-dy, x-dx, w-dw
    toBeIntegrated = varList[0] ** 0
    isFirstIntegral = True
    isSecondIntegral = True
    for i in (range(len(varList))):
        if (i != len(varList) - 1):
            #   check if integral is being calculated for first time and set limit accordingly
            if(isFirstIntegral):
                upperLimit = 1 + varList[len(varList) - 2]
                # print(upperLimit)
                # integrate("function, Integration variable, lowLimit, Up-limit")
                result = sp.integrate(toBeIntegrated, (varList[i], varList[i + 1], upperLimit))
                # print(toBeIntegrated, (varList[i], varList[i + 1], upperLimit))
                print(f"Integral wrt d{varList[i]}: {result}")
                isFirstIntegral = False
            elif(isSecondIntegral):
                upperLimit = 1 + varList[len(varList) - 1]
                # print(upperLimit)
                # integrate("function, Integration variable, lowLimit, Up-limit")
                result = sp.integrate(toBeIntegrated, (varList[i], varList[i + 1], upperLimit))
                # print(toBeIntegrated, (varList[i], varList[i + 1], upperLimit))
                print(f"Integral wrt d{varList[i]}: {result}")
                isSecondIntegral = False

            else:
                upperLimit = 1
                result = sp.integrate(toBeIntegrated, (varList[i], varList[i + 1], upperLimit))
                toBeIntegrated = result
                print(f"Integral wrt d{varList[i]}: {result}")
        else:
            # final integration with limits 0 to 1
            result = sp.integrate(toBeIntegrated, (varList[i], 0, 1))
            print(f"{len(varList)}-Variable X Integral value is: {result}")
    return result


def fiveVariableList():
    fiveVarList = [sp.Symbol('a'), sp.Symbol('z'), sp.Symbol('y'), sp.Symbol('x'), sp.Symbol('w')]
    return fiveVarList


def printTotalContribution(adjacencyMatrix, config, graphCount):

    typeOfIntegralCountArray = typeOfIntegralCount(adjacencyMatrix, config)
    fiveVarList = fiveVariableList()
    valueSigmaIntegralFivePoint = calcSigmaIntegral(fiveVarList)
    valueOmegaIntegralFivePoint = calcOmegaIntegral(fiveVarList)
    valueOmegaOmegaIntegralFivePoint = calcOmegaOmegaIntegral(fiveVarList)
    valueXIntegralFivePoint = calcXIntegral(fiveVarList)
    valueOmegaXIntegralFivePoint = calcOmegaXIntegral(fiveVarList)
    nameReferenceArray = ["Sigma", "Omega", "OmegaOmega", "X", "OmegaX"]
    valueSigmaIntegralFivePointArray = [valueSigmaIntegralFivePoint, valueOmegaIntegralFivePoint,
                                        valueOmegaOmegaIntegralFivePoint,
                                        valueXIntegralFivePoint, valueOmegaXIntegralFivePoint]
    for i in range(len(nameReferenceArray)):
        print(f"Total contribution of {nameReferenceArray[i]} integrals for Graph {graphCount} is: "
              f"{valueSigmaIntegralFivePointArray[i] * typeOfIntegralCountArray[i]}")
    graphCount += 1
    return graphCount


def main():

    config = [1, 2, 3, 4, 5]
    allPerms = permute(config)

    i = 0

    for perm in allPerms:
        i += 1
        print(perm)
    firstB5BiconnectedAdjacencyMatrix = firstB5Biconnected()
    secondB5BiconnectedAdjacencyMatrix = secondB5Biconnected()
    # print(i)
    graphCount = 1
    graphCount = printTotalContribution(firstB5BiconnectedAdjacencyMatrix, config, graphCount)
    # print(graphCount)
    # graphCount = printTotalContribution(secondB5BiconnectedAdjacencyMatrix, config, graphCount)
    #






main()
