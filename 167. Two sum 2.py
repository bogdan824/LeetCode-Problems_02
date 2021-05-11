def twoSum(numbers,target):
	first = 0
	last = len(numbers)-1
	while first<last:
		#is sum> target
		if numbers[first]+numbers[last]>target:
			last-=1
		elif numbers[first]+numbers[last]<target:
			first+=1
		else:
			return [first+1,last+1]

numbers = [2,3,4]
target = 6
print(twoSum(numbers,target))#sd
