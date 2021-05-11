num = 38
ss = 0
while num != 0:
	x = num%10
	ss+=x
	num=num//10
	if ss > 9 and num ==0:
		num=ss
		ss=0
print(ss) 

'''
	sum = 0
	while num != 0:
		x = num%10
		print("restul impartirii lui: "+str(num)+" la 10 este: "+ str(x))
		sum+=x
		num=num//10
		print("numarul ramas este: " + str(num))
		print()
	print("am ramas cu suma " + str(sum))
	print("-------------")

	if sum > 9:
		ifMare(sum)
	else:
		print("RETURNAM")
		print("suma este: " + str(sum))
		


print(ifMare(num))
'''