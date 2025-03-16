class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0]*(n+1)
        #write numbers from 1 to 9 in binary
        #observe that even numbers have the same number of 1s as their half
        #odd numbers have = number of 1s in their half + 1
        for i in range(1,n+1):
            if (i%2 == 1):
                dp[i] = dp[i//2]+1 #instead of i//2, i>>1 can also be used
            else:
                dp[i] = dp[i//2]    
        return dp
        