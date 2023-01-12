import sympy as sp


def calcSigmaIntegral(varList):
    # f-dz, g-dy, x-dx, w-dw
    toBeIntegrated = varList[0] ** 0
    for i in (range(len(varList))):
        if (i != len(varList)-1):
            result = sp.integrate(toBeIntegrated, (varList[i], varList[i + 1], 1))
            print(f"Integral wrt d{varList[i]}: {result}")
            toBeIntegrated = result
        else:
            result = sp.integrate(toBeIntegrated, (varList[i], 0, 1))
            print(f"{len(varList)}-Variable Sigma value is: {result}")


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
    calcSigmaIntegral(fourVarList)
    calcSigmaIntegral(fiveVarList)
    calcSigmaIntegral(sixVarList)
    calcSigmaIntegral(sevenVarList)
    calcSigmaIntegral(eightVarList)
    calcSigmaIntegral(nineVarList)
    calcSigmaIntegral(tenVarList)
    calcSigmaIntegral(elevenVarList)
    calcSigmaIntegral(twelveVarList)



main()
