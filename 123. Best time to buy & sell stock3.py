def bestTime3(prices):
	min_val = prices[0]
	max_sell = 0
	profit = []
	for i in range(1,len(prices)):
		min_val = min(min_val,prices[i])
		max_sell = prices[i] - min_val
		if max_sell > 1:
			profit.append(max_sell)
			max_sell = 0
			min_val = prices[i]
	profit.sort(reverse=True)
	if len(profit)==0:
            return 0
	elif len(profit)<=1:
		return profit[0]
	else:
		return profit[0]+profit[1]

prices = [7,6,4,3,1]

print(bestTime3(prices))