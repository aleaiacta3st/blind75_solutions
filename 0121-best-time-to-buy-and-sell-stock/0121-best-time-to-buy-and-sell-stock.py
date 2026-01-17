class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        max_profit=0
        global_min=float('inf')

        for i in range(n):
            if prices[i]<global_min:
                global_min=prices[i]
            curr_profit=prices[i]-global_min
            if max_profit<curr_profit:
                max_profit=curr_profit

        return max_profit
        