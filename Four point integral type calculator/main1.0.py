

def permute(arr):
	from itertools import permutations
	# Generate all permutations of the list
	perms = list(permutations(arr))
	# print("All permutaitons")
	result = []
	for perm in perms:
		# print(perm)
		result.append(perm)
	return result

def typeOfIntegral(adjacencyMatrix):
	print("works")



def main():

	firstB4Connected = [
		[0,1,2,3,4],
		[1,0,1,0,1],
		[2,1,0,1,0],
		[3,0,1,0,1],
		[4,1,0,1,0]
		]

	secondB4Connected = [
		[0,1,2,3,4],
		[1,0,1,0,1],
		[2,1,0,1,1],
		[3,0,1,0,1],
		[4,1,1,1,0]
		]

	thirdB4Connected = [
		[0,1,2,3,4],
		[1,0,1,1,1],
		[2,1,0,1,1],
		[3,1,1,0,1],
		[4,1,1,1,0]
		]
	config1 = [1,3,2,4];
	allPerms = permute(config1)
	firstPerm = allPerms[0]
	# print(len(allPerms))
	firstElementFirstPerm = firstPerm[0]
	thirdElementFirstPerm = firstPerm[2]
	# print(firstPerm)
	# print(thirdElementFirstPerm)
	# print(allPerms)
	# print(f"firstPerm: {firstPerm}")
	# print(f" firstElementFirstPerm: {firstElementFirstPerm}")

	# print(firstB4Connected)
	# test for sigma integrals
	i = 0;
	j = 0
	# perm will be an array, and perm[i] represents index i element in the array
	for perm in allPerms:
		# print(perm)
		# print(firstB4Connected[perm[0]][perm[len(perm)-1]])
		if(firstB4Connected[perm[0]][perm[len(perm)-1]] == 1):
			print(f"Sigma integral: {perm}")
			i += 1
		elif(firstB4Connected[perm[0]][perm[2]] == 1 ):
			print(f"Omega  integral: {perm}")
			j += 1

	print(f"No of sigma integrals is: {i}")
	print(f"No of omega integrals is: {j}")
	i = 0
	j = 0
	# add condition when
	for perm in allPerms:
		# print(perm)
		# print(firstB4Connected[perm[0]][perm[len(perm)-1]])
		if(secondB4Connected[perm[0]][perm[len(perm)-1]] == 1):
			print(f"Sigma integral: {perm}")
			i += 1
		elif(secondB4Connected[perm[0]][perm[2]] == 1 ):
			print(f"Omega  integral: {perm}")
			j += 1
	print(f"No of sigma integrals is: {i}")
	print(f"No of omega integrals is: {j}")

	i = 0
	j = 0
	# add condition when
	for perm in allPerms:
		# print(perm)
		# print(firstB4Connected[perm[0]][perm[len(perm)-1]])
		if(thirdB4Connected[perm[0]][perm[len(perm)-1]] == 1):
			print(f"Sigma integral: {perm}")
			i += 1
		elif(thirdB4Connected[perm[0]][perm[2]] == 1 ):
			print(f"Omega  integral: {perm}")
			j += 1
	print(f"No of sigma integrals is: {i}")
	print(f"No of omega integrals is: {j}")
main()
