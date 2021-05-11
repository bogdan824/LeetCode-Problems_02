'''
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), 
some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
'''

def findDuplicates(nums):
	nums.sort()
	keep = {}
	hold = []
	for i in range(len(nums)):
		if nums[i] in keep:
			keep[nums[i]]+=1
		else:
			keep[nums[i]]=1

	for k,v in keep.items():
		if v>1:
			hold.append(k)
	return hold

nums=[4,3,2,7,8,2,3,1]
print(findDuplicates(nums))