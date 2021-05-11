def countSegments(s):
	s = s.lstrip()
	s = s.rstrip()
	count = 1
	for i in range (len(s)):
		if s[i]==" " and s[i+1]!=" ":
			count+=1
	return count



s = ", , , ,        a, eaefa"
print(countSegments(s))