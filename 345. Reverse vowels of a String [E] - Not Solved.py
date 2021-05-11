'''
Date: 05.04.21
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.
'''

# NOT SOLVED - Needs to be reattended
def reverseVow(s):
	vowels = ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]
	keep = []
	for x in range(len(s)):
		keep.append(s[x])
	i = 0
	j = len(keep)-1
	while i<j:
		
		if keep[i] not in vowels:
			i+=1
		if keep[j] not in vowels:
			j-=1

		if keep[i] in vowels and keep[j] in vowels:
			keep[i],keep[j]=keep[j],keep[i]
			i+=1
			j-=1
	hold = ""
	for i in range (len(keep)):
		hold += keep[i]

	return hold
#s = "hello"
#s = "leetcode"
s = "......a....."
print(reverseVow(s))