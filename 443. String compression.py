'''
Given an array of characters chars, compress it using the following algorithm:
Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.
'''
def compress(chars):
	chars.append("")
	keep = []
	count = 0
	for i in range(len(chars)-1):
		if chars[i] == chars[i+1]:
			count+=1
	
		else:
			keep.append(chars[i])
			if count>1:
				keep.append(str(count))
			count=1
	
	return keep

chars = ["a","b","b","c","c","c"]
print(compress(chars))