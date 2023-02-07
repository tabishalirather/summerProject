# import s''y''mp''y'' as sp
# varList = [0, sp.S''y''mbol('''w'''), sp.S''y''mbol('''x'''), sp.S''y''mbol('''y''')]
sortedLimitArray = [[('y', 1), ('x', 1), ('w', 1), 1/6], (('y', 'w + 1'), ('x', 1), ('w', 1), 1/3), (('y', 1), ('x', 1), ('w', 1), 1/6), (('y', 1), ('x', 1), ('w', 1), 1/6), (('y', 'w + 1'), ('x', 1), ('w', 1), 1/3), (('y', 1), ('x', 1), ('w', 1), 1/6), (('y', 'w + 1'), ('x', 1), ('w', 1), 1/3), (('y', 1), ('x', 1), ('w', 1), 1/6), (('y', 'w + 1'), ('x', 1), ('w', 1), 1/3), (('y', 1), ('x', 1), ('w', 1), 1/6), (('y', 1), ('x', 1), ('w', 1), 1/6), (('y', 1), ('x', 1), ('w', 1), 1/6), (('y', 1), ('x', 1), ('w', 1), 1/6), (('y', 1), ('x', 1), ('w', 1), 1/6), (('y', 1), ('x', 1), ('w', 1), 1/6), (('y', 'w + 1'), ('x', 1), ('w', 1), 1/3), (('y', 1), ('x', 1), ('w', 1), 1/6), (('y', 'w + 1'), ('x', 1), ('w', 1), 1/3), (('y', 1), ('x', 1), ('w', 1), 1/6), (('y', 'w + 1'), ('x', 1), ('w', 1), 1/3), (('y', 1), ('x', 1), ('w', 1), 1/6), (('y', 1), ('x', 1), ('w', 1), 1/6), (('y', 'w + 1'), ('x', 1), ('w', 1), 1/3), (('y', 1), ('x', 1), ('w', 1), 1/6)]
newArray = []

# print(sortedLimitArray[0][3])
for subArray in sortedLimitArray:
    # print(subArray.index(('y', 1), ('x', 1), ('w', 1)))
    subArray = list(subArray)
    subArray.pop(3)
    print(subArray)
    newArray.append(subArray)

print(newArray)
# print(sortedLimitArray)
# myDict = dict(sortedLimitArray[0][3] = sorted())