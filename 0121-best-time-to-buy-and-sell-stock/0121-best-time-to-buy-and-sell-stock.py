class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        minprice = prices[0]
        for i in prices:
            minprice = min(minprice,i)
            profit = max(profit, (i-minprice))
        return profit
        
        