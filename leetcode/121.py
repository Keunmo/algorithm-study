# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(prices):
    profit=0
    for i in range(len(prices)):
        print(i)
        print('max',max(prices[i:]))
        if i == len(prices)-1:
            break
        if max(prices[i:]) - prices[i] > profit:
            profit = max(prices[i:]) - prices[i]
    print(profit)
    return profit

maxProfit([1,2])