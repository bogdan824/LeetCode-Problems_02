def climbStaris(n):
	path = {1:1 ,2:2, 3:3}
	for i in range (4 , n+1):
		path[i] = path[i-1]+path[i-2]
	return path[n]

print(climbStaris(5))