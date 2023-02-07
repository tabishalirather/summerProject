import sympy as sp


# turns out xIntegral is same as omegaIntegral
def calcOmegaXIntegral(varList):
    # f-dz, g-dy, x-dx, w-dw
    toBeIntegrated = varList[0] ** 0
    isFirstIntegral = True
    isSecondIntegral = True
    for i in (range(len(varList))):
        if (i != len(varList) - 1):
            # check if integral is being calculated for first time and set limit accordingly
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


def main():
    fourVarList = [sp.Symbol('z'), sp.Symbol('y'), sp.Symbol('x'), sp.Symbol('w')]
    fiveVarList = [sp.Symbol('a'), sp.Symbol('z'), sp.Symbol('y'), sp.Symbol('x'), sp.Symbol('w')]
    sixVarList = [sp.Symbol('b'), sp.Symbol('a'), sp.Symbol('z'), sp.Symbol('y'), sp.Symbol('x'), sp.Symbol('w')]
    sevenVarList = [sp.Symbol('c'), sp.Symbol('b'), sp.Symbol('a'), sp.Symbol('z'), sp.Symbol('y'),
                    sp.Symbol('x'), sp.Symbol('w')]
    eightVarList = [sp.Symbol('d'), sp.Symbol('c'), sp.Symbol('b'), sp.Symbol('a'), sp.Symbol('z'), sp.Symbol('y'),
                    sp.Symbol('x'), sp.Symbol('w')]
    nineVarList = [sp.Symbol('e'), sp.Symbol('d'), sp.Symbol('c'), sp.Symbol('b'), sp.Symbol('a'), sp.Symbol('z'),
                   sp.Symbol('y'),
                   sp.Symbol('x'), sp.Symbol('w')]
    tenVarList = [sp.Symbol('f'), sp.Symbol('e'), sp.Symbol('d'), sp.Symbol('c'), sp.Symbol('b'), sp.Symbol('a'),
                  sp.Symbol('z'),
                  sp.Symbol('y'),
                  sp.Symbol('x'), sp.Symbol('w')]
    elevenVarList = [sp.Symbol('g'), sp.Symbol('f'), sp.Symbol('e'), sp.Symbol('d'), sp.Symbol('c'), sp.Symbol('b'),
                     sp.Symbol('a'),
                     sp.Symbol('z'),
                     sp.Symbol('y'),
                     sp.Symbol('x'), sp.Symbol('w')]
    twelveVarList = [sp.Symbol('h'), sp.Symbol('g'), sp.Symbol('f'), sp.Symbol('e'), sp.Symbol('d'), sp.Symbol('c'),
                     sp.Symbol('b'),
                     sp.Symbol('a'),
                     sp.Symbol('z'),
                     sp.Symbol('y'),
                     sp.Symbol('x'), sp.Symbol('w')]
    # calcOmegaXIntegral(fourVarList)
    calcOmegaXIntegral(fiveVarList)
    calcOmegaXIntegral(sixVarList)
    calcOmegaXIntegral(sevenVarList)
    calcOmegaXIntegral(eightVarList)
    calcOmegaXIntegral(nineVarList)
    calcOmegaXIntegral(tenVarList)
    calcOmegaXIntegral(elevenVarList)
    calcOmegaXIntegral(twelveVarList)


main()
