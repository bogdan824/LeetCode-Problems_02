def isPalindrome(s):
	s = s.lower()
	holdit = ""
	for charac in s:
		if charac.isalpha():
			holdit+=charac
	i=0
	j=len(holdit)-1
	while i<=j:
		if holdit[i]!=holdit[j]:
			return False
		i+=1
		j-=1
	return True
		


s = "0P"
print(isPalindrome(s))