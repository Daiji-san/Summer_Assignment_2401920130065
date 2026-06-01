#Problem Link --> https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#Description --> You are given an array prices where prices[i] is the price of a given stock on the ith day.
#                You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#                Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution(object):
    def maxProfit(self, prices):
        left_ptr = 0 
        right_ptr = 1 
        max_profit = 0
        
        while right_ptr < len(prices):
            if prices[left_ptr] < prices[right_ptr]:
                current_profit = prices[right_ptr] - prices[left_ptr]
                max_profit = max(current_profit, max_profit)
            else:
                left_ptr = right_ptr    
            right_ptr += 1
        return max_profit
