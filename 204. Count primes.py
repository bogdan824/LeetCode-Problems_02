def countPrim(n):
	keep = []
	for i in range(n+1):
		keep.append(i)

	for i in range(n+1):
		j=i
		while j*i<n:
			print()
	print(keep)

n = 10
print(countPrim(n))