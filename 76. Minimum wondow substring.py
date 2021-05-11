def minSubs(s,t):
	x = sorted(s)
	y = sorted(t)

	if y in x:
		print("da")
	

s = "ADOBECODEBANC"
t = "ABC"
print(minSubs(s,t))