n = 19
suma = 0
while n != 0:
	x=(n%10)**2
	suma+=x
	
	n//=10
	if suma != 1:
		n = suma
		suma = 0
return 1



