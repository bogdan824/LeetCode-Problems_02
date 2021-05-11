def distributeCandies(candyType):
	allowance = len(candyType)//2
	canEat = 0
	hashm = {}
	for i in candyType:
		if i in hashm.keys():
			hashm[i]+=1
		else:
			hashm[i]=1
	for k,v in hashm.items():
		if canEat < allowance:
			canEat+=1
	return canEat


candyType = [1,1,2,2,3,3,3,3]
print(distributeCandies(candyType))