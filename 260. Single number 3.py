def singleNum(nums):
	keep = []
	hashm = {}
	for num in nums:
		if num in hashm.keys():
			hashm[num]+=1
		else:
			hashm[num]=1
	for k,v in hashm.items():
		if v == 1:
			keep.append(k)
	return keep


nums = [1,2,1,3,2,5]
print(singleNum(nums))