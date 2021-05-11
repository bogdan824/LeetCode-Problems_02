def factorialTrail(n):
	total = 1
	count = 0
	while n!=0:
		#print("total",total,"*n",n)
		total*=n
		n-=1
	while total%10 == 0:
		count+=1
		total//=10
	return count

n = 10
print(factorialTrail(n))

