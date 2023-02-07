# original_arr = [[1, 2, 3], [3, 2, 1], [4, 5, 6], [1, 2, 3], [7, 8, 9]]
# unique_arr = []
#
# for sub_array in original_arr:
#     if sub_array not in unique_arr:
#         unique_arr.append(sub_array)
#
# print(unique_arr)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
grouped_list = []
subgroup = []
for i, x in enumerate(my_list):
    subgroup.append(x)
    if (i+1) % 3 == 0 and (i+1) % 4 != 0:
        grouped_list.append(subgroup)
        subgroup = []
    if (i+1) % 4 == 0:
        grouped_list.append([x])

print(grouped_list)

