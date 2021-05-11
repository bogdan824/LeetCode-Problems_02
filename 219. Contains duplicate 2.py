def contDup2(nums,k):
	hashm = {}
	for i in range(len(nums)):
		curr = nums[i]
		if curr in hashm and k>=i-hashm[curr]:
			
			return True
		else:
			hashm[curr]=i
	return False

nums = [1,2,3,1]
k = 3	
print(contDup2(nums,k))