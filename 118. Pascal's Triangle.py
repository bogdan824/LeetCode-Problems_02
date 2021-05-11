def pasTriangle(numRows):
	a = [[] for i in range(numRows+1)]
	for i in range(numRows+1):
		for j in range(i+1):
			if j<i:
				if j==0:
					a[i].append(1)
				else:
					a[i].append(a[i-1][j]+a[i-1][j-1])
			elif j==i:
				a[i].append(1)

	return a[numRows]

numRows=5
print(pasTriangle(numRows))