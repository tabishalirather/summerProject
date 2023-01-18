import itertools

# Adjacency matrix
adj_matrix = [[0, 1, 1, 0, 0, 1],
              [1, 0, 1, 0, 0, 1],
              [1, 1, 0, 1, 0, 0],
              [0, 0, 1, 0, 1, 0],
              [0, 0, 0, 1, 0, 1],
              [1, 1, 0, 0, 1, 0]]

# Linear combination
lin_comb = [1, 2, 4, 5, 3]

# Get all permutations of the linear combination
permutations = list(itertools.permutations(lin_comb))

# Set to store unique integrals
unique_integrals = set()

# Iterate through permutations
for perm in permutations:
    # Initialize the integral string
    integral = ""
    # Iterate through nodes in the permutation
    for i in range(len(perm)):
        # Get the next node in the permutation
        next_node = perm[(i+1) % len(perm)]
        # Check if there is an edge between the current node and the next node
        if adj_matrix[perm[i]][next_node] == 1:
            # Append the limits of the integral
            integral += str(perm[i]) + "," + str(next_node) + ","
    # Add the integral to the set of unique integrals
    unique_integrals.add(integral)

# Print the set of unique integrals
print(unique_integrals)
