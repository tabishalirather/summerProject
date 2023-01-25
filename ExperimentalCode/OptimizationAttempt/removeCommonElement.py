original_arr = [[1, 2, 3], [3, 2, 1], [4, 5, 6], [1, 2, 3], [7, 8, 9]]
unique_arr = []

for sub_array in original_arr:
    if sub_array not in unique_arr:
        unique_arr.append(sub_array)

print(unique_arr)
