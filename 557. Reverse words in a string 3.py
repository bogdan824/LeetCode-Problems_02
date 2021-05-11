'''
557. Given a string s, reverse the order of characters in each word within a sentence 
while still preserving whitespace and initial word order.
'''

def reverseWords(s):
	keep = []
	hold = ""
	start = 0
	for i in range (len(s)):
		if s[i]==" " or None:
			stop = i
			keep.append(s[start:stop])
			start = i+1
	keep.append(s[start:len(s)])
	for i in range(len(keep)):
		keep[i]=keep[i][::-1]
		hold+=keep[i]+" "
	return (hold[0:-1])
s = "Let's take LeetCode contest"
print(reverseWords(s))