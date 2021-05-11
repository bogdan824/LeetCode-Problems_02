def moveZero(nums):
	anchor = 0
	for i in range(len(nums)):
		#print("nums",nums[i],"anchor",anchor)
		if nums[i]!=0:
			keep = nums[anchor]
			nums[anchor] = nums[i]
			nums[i] = keep
			anchor+=1
		
	return nums



nums = [0,1,0,3,12]
print(moveZero(nums))