def findDiff(s,t):
	if s=="":
		return t

	hashm = {}
	for i in s:
		if i in hashm:
			hashm[i]+=1
		else:
			hashm[i]= 1
	for i in t:
		if i in hashm:
			hashm[i]+=1
		else:
			hashm[i]= 1			
	for k,v in hashm.items():
		if v%2==1:
			return k
	
	
s = "abc"
t = "abcd"
print(findDiff(s,t))