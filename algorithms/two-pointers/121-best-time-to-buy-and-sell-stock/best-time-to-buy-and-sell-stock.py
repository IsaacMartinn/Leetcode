class Solution:
    def maxProfit(self, prices):
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            curr_profit = prices[r] - prices[l]
            if prices[r] < prices[l]: 
                l = r
            else:
                max_profit = max(curr_profit, max_profit)
            r += 1
        return max_profit
