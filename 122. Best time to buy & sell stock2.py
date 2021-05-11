def bestTime2(prices):
	min_val = prices[0]
	max_sell = 0
	profit = 0
	for i in range(1,len(prices)):
		min_val = min(min_val,prices[i])
		max_sell = prices[i] - min_val
		if max_sell > 0:
			profit+=max_sell
			max_sell = 0
			min_val = prices[i]
	return profit

#prices = [7,1,5,3,6,4]
prices = [1,2,3,4,5]

print(bestTime2(prices))