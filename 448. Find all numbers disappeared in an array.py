'''
Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear in nums.
'''

def findNums(nums):
	keep = []
	for i in range (len(nums)):
		j = abs(nums[i])-1
		nums[j] = abs(nums[j])* -1

	for i in range(len(nums)):
		if nums[i]>0:
			keep.append(i+1)
	return keep


	
nums = [4,3,2,7,8,2,3,1]
print(findNums(nums))