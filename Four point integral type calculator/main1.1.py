# Finds out all the linear permutations, given any one permutation. Then from the adjacency matrix, it determines
# which linear integral corresponds to which type of  integral

# fxn to figure out all the permutations of a given configuration
def permute(arr):
    from itertools import permutations
    # Generate all permutations of the list
    perms = list(permutations(arr))
    # print("All permutations")
    result = []
    for perm in perms:
        # print(perm)
        result.append(perm)
    return result


# fxn to determine which linear combination corresponds to which type of integral
def typeOfIntegral(adjacencyMatrix, anyParticularConfig):
    i = 0
    j = 0
    allPerms = permute(anyParticularConfig)
    # perm will be an array, and perm[i] represents index i element in the array
    for perm in allPerms:
        # print(perm)
        # print(firstB4Connected[perm[0]][perm[len(perm)-1]])
        if adjacencyMatrix[perm[0]][perm[len(perm) - 1]] == 1:
            print(f"Sigma integral: {perm}")
            i += 1
        elif adjacencyMatrix[perm[0]][perm[len(perm) - 2]] == 1:
            print(f"Omega  integral: {perm}")
            j += 1

    print(f"No of sigma integrals is: {i}")
    print(f"No of omega integrals is: {j}")
    print("\n")


def firstB4Biconnected():
    firstB4Graph = [
        [0, 1, 2, 3, 4],
        [1, 0, 1, 0, 1],
        [2, 1, 0, 1, 0],
        [3, 0, 1, 0, 1],
        [4, 1, 0, 1, 0]
    ]
    return firstB4Graph


def secondB4Biconnected():
    secondB4Graph = [
        [0, 1, 2, 3, 4],
        [1, 0, 1, 0, 1],
        [2, 1, 0, 1, 1],
        [3, 0, 1, 0, 1],
        [4, 1, 1, 1, 0]
    ]
    return secondB4Graph


def thirdB4BiConnected():
    thirdGraph = [
        [0, 1, 2, 3, 4],
        [1, 0, 1, 1, 1],
        [2, 1, 0, 1, 1],
        [3, 1, 1, 0, 1],
        [4, 1, 1, 1, 0]
    ]
    return thirdGraph


def main():
    firstGraphB4 = firstB4Biconnected()
    secondGraphB4 = secondB4Biconnected()
    thirdGraphB4 = thirdB4BiConnected()
    config = [1, 2, 3, 4];
    typeOfIntegral(firstGraphB4, config)
    typeOfIntegral(secondGraphB4, config)
    typeOfIntegral(thirdGraphB4, config)


main()
