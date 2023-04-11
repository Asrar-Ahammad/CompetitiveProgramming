def max_profit(prices):
    # min = prices[0]
    # max = prices[0]
    # for i in prices:
    #     if i < min:
    #         min = i
    #         max = i
    #     if i > max:
    #         max = i
    # return max - min

    min_price = max(prices)
    profit = 0
    for i in prices:
        if i < min_price:
            min_price = i
        if i-min_price > profit:
            profit = i-min_price
    return profit


prices = [7,6,4,3,1]
print(max_profit(prices))