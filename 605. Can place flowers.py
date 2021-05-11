def canPlace(flowerbed,n):
	count = 0
	if flowerbed[0]!=1 and flowerbed[1]!=1:
		flowerbed[0]=1
		count+=1
	for i in range (1,len(flowerbed)-1):
		if flowerbed[i] == 0 and flowerbed[i-1]!=1 and flowerbed[i+1]!=1:
			flowerbed[i]=1
			count+=1
	if flowerbed[-2]==0 and flowerbed[-1]==0:
		flowerbed[-1]=1
		count+=1
	if count>=n:
		return True
	return False
	------


flowerbed = [1,0,0,0,1]
n = 1
print(canPlace(flowerbed,n))