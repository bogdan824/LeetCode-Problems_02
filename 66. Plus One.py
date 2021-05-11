#Given a non-empty array of decimal digits representing a non-negative integer,
# increment one to the integer. The digits are stored such that the most significant
# digit is at the head of the list, and each element in the array contains a single digit.
#You may assume the integer does not contain any leading zero, except the number 0 itself.
def plus_one(digits):
	suma = 0
	for i in  range (len(digits)):
		suma = suma * 10 + digits[i]
	suma+=1
	keep = []
	while suma != 0:
		keep.append(suma%10)
		suma//=10
	rev = keep[::-1]
	return rev
	


digits = [1,2,3]
print(plus_one(digits))