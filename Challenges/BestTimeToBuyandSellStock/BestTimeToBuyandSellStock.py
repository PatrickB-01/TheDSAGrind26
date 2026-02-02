"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4
"""


from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxW = 0
        window=[0,1]
        windowSize = 1
        if len(prices)==1:
            return maxW
        
        is_sorted_desc= False
        while windowSize <= len(prices):
            if prices[window[0]] < prices[window[1]]:
                win = prices[window[1]] - prices[window[0]]
                if win > maxW:
                    maxW = win
            
            if windowSize==1:
                is_sorted_desc= is_sorted_desc and (prices[window[0]] > prices[window[1]])

            if windowSize==2 and is_sorted_desc:
                return maxW

            if window[1] != len(prices)-1:
                window[0]+=1
                window[1]+=1
            else:
                windowSize+=1
                window[0]=0
                window[1]= windowSize-1
        return maxW
    
    # too much time

    def maxProfit2(self, prices: List[int]) -> int:
        maxW = 0
        window=[0,1]
        if len(prices)==1:
            return maxW
        
        while window[1] < len(prices)-1:
            if prices[window[0]] < prices[window[1]]:
                win = prices[window[1]] - prices[window[0]]
                if win > maxW:
                    maxW = win
            
            if prices[window[0]] > prices[window[1]]:
                window[0] = window[1]

            #if window[1] != len(prices)-1:
            window[1]+=1
        return maxW
    # the solution