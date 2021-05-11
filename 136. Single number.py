def singleNum(nums):
	hashm = {}
	for num in nums:
		if num in hashm:
			hashm[num]+=1
		else:
			hashm[num]=1
	for k,v in hashm.items():
		if v == 1:
			return k
nums = [2,2,1]
print(singleNum(nums))