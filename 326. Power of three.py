def power3(n):
	for i in range (32):
		if 3**i == n:
			return True
	return False


n = 9
print(power3(n))