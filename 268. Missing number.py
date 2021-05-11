def missingNum(nums):
	nums.sort()
	for i in range(len(nums)):
		if i != nums[i]:
			return i
	return len(nums)

nums = [3,0,1]
print(missingNum(nums))