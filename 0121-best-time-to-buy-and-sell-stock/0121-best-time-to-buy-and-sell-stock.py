class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        max_profit = 0
        global_min_price = float('inf')
        for i in range(n):
            if prices[i]<global_min_price:
                global_min_price = prices[i]
            current_profit = prices[i] - global_min_price
            if current_profit > max_profit:
                max_profit = current_profit
        return max_profit

        