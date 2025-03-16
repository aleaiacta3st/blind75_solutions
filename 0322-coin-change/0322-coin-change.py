class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        
        
        for i in range(1, len(dp)): 
            for j in coins:
                if (i-j>=0):#if we are making an amount i=10, 
                            # a coin with j=15 need not be considered
                    dp[i] = min(dp[i], 1+(dp[i-j]))
        
        if dp[amount]==float('inf'):
            return -1
        else:
            return dp[amount]

    # assume coin denominations are 1,2,5,10
    # find the minimum number of coins that make up 0
    # find the minimum number of coins that make up 1
    # find the minimum number of coins that make up 2
    # -----------------------------------------------
    # find the minimum number of coins that make up the target amount

    # suppose the coin denominations are 1,2,5 and 10
    # In how minimum number of coins can a target amount i be reached?
    # The last coin we choose can be 1,2,5, or 10
    # If we choose 1, the minimum number of coins to reach i is 1+minimum number of coins to reach i-1
    # If we choose 2, the minimum number of coins to reach i is 1+minimum number of coins to reach i-2
    # If we choose 5, the minimum number of coins to reach i is 1+minimum number of coins to reach i-5
    # If we choose 10, the minimum number of coins to reach i is 1+minimum number of coins to reach i-10
    # The +1 is for the coin finally chosen to make the target amount i
    # either 1,2 5, or 10 can be chosen
    # so we take the minimum of the 4 values calculated earlier
    # mathematically, the recurrence relation looks like this - w(i) = min(w(i-1),w(i-2),w(i-5),w(i-10))
    # but when we put it in code it looks like below
    # dp[i] = min(dp[i], 1+(dp[i-j]))
    # This is because The code is comparing the current best solution with a 
    # new candidate solution as we iterate through each coin.

    #if dp[amount] is still inf, it means that task is impossible. No combo of coins can make up that amount. 
    # in that case return -1 as asked.

    #the difference between needing 0 coins and infinite number of coins
    #dp[0] = 0 is a valid solution (we need 0 coins to make 0).
    #dp[amount] = inf means it's impossible to make that amount with the given coins, and we return -1.
        
        