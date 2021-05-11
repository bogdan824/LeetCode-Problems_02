def bestTime(prices):
	min_val = prices[0]
	max_profit = 0
	for i in range(1,len(prices)):
		#print("avem valoarea minima",min_val, ". comparam cu",prices[i])
		min_val = min(min_val,prices[i])
		#print("am ales",min_val)
		max_profit = max(max_profit,prices[i]-min_val)
		#print("max_profit este",max_profit)

	return max_profit
		
		
prices = [7,1,5,3,6,4]
#prices = [7,6,4,3,1]

print(bestTime(prices))