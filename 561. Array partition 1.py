def arrayPartition(nums):
	nums.sort()
	suma=0
	for i in range(0,len(nums),2):
		suma+=min(nums[i],nums[i+1])
	return suma

nums = [1,4,3,2]
print(arrayPartition(nums))