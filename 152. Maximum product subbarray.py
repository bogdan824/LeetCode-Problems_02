def maxProd(nums):
	maxi = nums[0]
	curr_max = nums[0]
	curr_min = nums[0]
	
	for i in range (1,len(nums)):
		if nums[i]==0:
			curr_max = 1
			curr_min = 1
		
		curr_max = max(nums[i]*curr_max, nums[i]*curr_min, nums[i])
		curr_min = min(curr_max * nums[i], nums[i]*curr_min, nums[i])
		maxi = max(maxi,curr_max)
		

	return maxi

nums = [2,3,-2,4]
print(maxProd(nums))