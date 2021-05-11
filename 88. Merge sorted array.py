def merge(nums1, nums2, m,n):
	x = 0
	for i in range (m,n+m):
		nums1[i]=nums2[x]
		x+=1
	nums1.sort()
	return nums1




nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m=3
n=3
print(merge(nums1,nums2,m,n))