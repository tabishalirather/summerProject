import sympy as sp


def manualOmegaCalculator():
    fiveVarList = [sp.Symbol('a'), sp.Symbol('z'), sp.Symbol('y'), sp.Symbol('x'), sp.Symbol('w')]
    toBeIntegrated = fiveVarList[0]


def calcOmegaOmegaIntegral(varList):
    # f-dz, g-dy, x-dx, w-dw
    toBeIntegrated = varList[0] ** 0
    print(len(varList))
    for i in (range(len(varList))):
        if (i != len(varList) - 1):
            result = sp.integrate(toBeIntegrated, (varList[i], varList[i + 1], 1))
            print(f"Integral wrt d{varList[i]}: {result}")
            toBeIntegrated = result
        else:
            result = sp.integrate(toBeIntegrated, (varList[i], 0, 1))
            print(f"{len(varList)}-Variable Sima value is: {result}")


def main():
    fourVarList = [sp.Symbol('z'), sp.Symbol('y'), sp.Symbol('x'), sp.Symbol('w')]
    fiveVarList = [sp.Symbol('z'), sp.Symbol('y'), sp.Symbol('x'), sp.Symbol('w'), sp.Symbol('a')]
    sixVarList = [sp.Symbol('z'), sp.Symbol('y'), sp.Symbol('x'), sp.Symbol('w'), sp.Symbol('a'), sp.Symbol('b')]
    sevenVarList = [sp.Symbol('z'), sp.Symbol('y'), sp.Symbol('x'), sp.Symbol('w'), sp.Symbol('a'), sp.Symbol('b'),
                    sp.Symbol('c')]
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
    calcOmegaOmegaIntegral(fourVarList)
    calcOmegaOmegaIntegral(fiveVarList)
    calcOmegaOmegaIntegral(sixVarList)
    calcOmegaOmegaIntegral(sevenVarList)
    calcOmegaOmegaIntegral(eightVarList)
    calcOmegaOmegaIntegral(nineVarList)
    calcOmegaOmegaIntegral(tenVarList)
    calcOmegaOmegaIntegral(elevenVarList)
    calcOmegaOmegaIntegral(twelveVarList)
    print("This is omegaOmega in experiment branch")


main()
