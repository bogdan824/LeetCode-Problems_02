def majElem(nums):
	hashm = {}
	for i in nums:
		if i in hashm.keys():
			hashm[i]+=1
		else:
			hashm[i]=1
	for k,v in hashm.items():
		if v >= len(nums)/2:
			return v


nums = [3,2,3]
print(majElem(nums))