c=1
i=0 
bool = False
for i in range(c+1):
	for j in range (c+1):
		if(((i**2)+(j**2))==c):
			bool = True
print(bool)