class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        #the answer we need is dp[n]. Therefore we need the 
        # array length to be n+1 
        dp[0]=1 #you are already at the destination. 
                #imagine the only way to reach the destination 
                # is by staying there. That is the only way.
        dp[1]=1 #when you are only 1 step away from destination, 
                #the only way to reach the destination is by choosing 
                # a single step.
        #recognizing that to reach stair i, you can only get there by:
        #   Taking a 1-step from stair i-1
        #   Taking a 2-step from stair i-2
        #   dp[i] = dp[i-1] + dp[i-2]
        #the last step can be a single step or a double step
        # if the last step is a single step, 
        #   # of ways to reach the destination = # of ways to take n-1 steps
        # if the last step is a single step, 
        #   # of ways to reach the destination = # of ways to take n-1 steps
        ## of ways to complete n steps = 
        # # of ways to take n-1 steps + # of ways to take n-2 steps
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
            #dp[i] is the number of ways to climb exactly i stairs
        return dp[n]
        