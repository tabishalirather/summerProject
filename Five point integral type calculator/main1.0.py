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


def typeOfIntegral(adjacencyMatrix, anyParticularConfig):
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
        if (adjacencyMatrix[perm[0]][perm[len(perm) - 1]] == 1):
            print(f"Sigma integral: {perm}")
            sigmaCount += 1
        elif (adjacencyMatrix[perm[0]][perm[len(perm) - 2]] and adjacencyMatrix[perm[1]][perm[len(perm) - 1]] == 1):
            print(f"Omega  integral: {perm}")
            wCount += 1
        elif(adjacencyMatrix[perm[0]][perm[len(perm) - 3]] and adjacencyMatrix[perm[1]][perm[len(perm) - 1]] == 1):
            print(f"ww integral: {perm}")
            wwCount += 1
        elif(adjacencyMatrix[perm[0]][perm[len(perm) - 2]] and adjacencyMatrix[perm[2]][perm[len(perm) - 1]] == 1):
            print(f"x integral: {perm}")
            xCount += 1
        elif(adjacencyMatrix[perm[0]][perm[len(perm) - 3]] and adjacencyMatrix[perm[1]][perm[len(perm) - 2]] == 1 and
             adjacencyMatrix[perm[2]][perm[len(perm) - 1]] == 1):
            print(f"wx integral: {perm}")
            wxCount += 1

    # print(len(perm))
    print(f"No of sigma integrals is: {sigmaCount}")
    print(f"No of omega integrals is: {wCount}")
    print(f"No of ww integrals is: {wwCount}")
    print(f"No of x integrals is: {xCount}")
    print(f"No of wx integrals is: {xCount}")
    print("\n")


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
        [1, 0, 1, 0, 0, 1],
        [2, 1, 0, 1, 0, 0],
        [3, 0, 1, 0, 1, 0],
        [4, 0, 0, 1, 0, 1],
        [5, 1, 0, 0, 1, 0]
    ]
    return secondB5Graph


def main():
    config = [1, 2, 3, 4, 5]

    allPerms = permute(config)
    i = 0
    for perm in allPerms:
        i += 1
        print(perm)

    print(i)
    firstGraphB5 = firstB5Biconnected()
    typeOfIntegral(firstGraphB5, config)
    # focus on calculating the actual value of the integral, graph isomorphism and type generation will be dealt with later


main()
