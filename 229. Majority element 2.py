def majElem(nums):
	hashm = {}
	keep = []
	for i in nums:
		if i in hashm.keys():
			hashm[i]+=1
		else:
			hashm[i]=1

	for k,v in hashm.items():
		#print("k is",k,"v is",v)
		if v > round(len(nums)//3):
			keep.append(k)
	return keep

nums = [3,2,3]
print(majElem(nums))