# Problem

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Constraints:

1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4


# Attempt 1

```py
def maxProfit( prices: list[int]) -> int:
    if len(prices)<2:
        return 0
    k=2
    profit = prices[1] - prices[0]
    max_profit = profit

    while k<=len(prices):
        for i in range(len(prices)-k+1):
            profit = prices[i+k-1] - prices[i]
            max_profit = max(max_profit,profit)
        k+=1

    return max_profit if max_profit > 0 else 0
```


# Attempt 2

# Solution

```py
def maxProfit( prices: list[int]) -> int:
    if len(prices)<2:
        return 0

    buy_price = prices[0]
    max_profit = 0

    for i in range(1,len(prices)):
        if prices[i]<buy_price:
            buy_price = prices[i]
        else:
            profit = prices[i] - buy_price
            max_profit = max(max_profit,profit)


    return max_profit if max_profit > 0 else 0
```

keep the lowest buy price and move pointer while keeping track of max profit