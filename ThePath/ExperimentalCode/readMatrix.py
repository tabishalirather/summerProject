matrix = []
with open("matrix.txt", "r") as file:
    for line in file:
        matrix.append([int(x) for x in line.strip().split()])

new_matrix = [[i + 1] + row for i, row in enumerate(matrix)]
new_matrix.insert(0, [0, 1, 2, 3, 4, 5])
print(new_matrix)
