'''
Given an integer array nums, return an array answer such that answer[i] is equal to the
product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
'''

def arrProd(nums):
	keep = []
	prod = 1
	for i in range(len(nums)):
		keep.append(prod)
		prod *= nums[i]
	
	prod = 1
	for j in range(len(nums)-1,-1,-1):
		keep[j] *= prod
		prod *= nums[j]
	return keep
#nums = [-1,1,0,-3,3]
#nums = [1,2,3,4]
nums = [0,0]
print(arrProd(nums))