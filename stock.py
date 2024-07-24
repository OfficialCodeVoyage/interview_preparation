# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


def sell_stock(stocks):
    position = -1
    for i in stocks:
        if i == 1:
            position = stocks[i]

    stocks1 = stocks[position:]

    max_val = max(stocks1)

    profit = max_val - 1

    return profit


prices = [7, 1, 5, 3, 6, 4]

print(sell_stock(prices))
