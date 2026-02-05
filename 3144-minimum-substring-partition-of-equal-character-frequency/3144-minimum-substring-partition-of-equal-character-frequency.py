class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:

        n=len(s)

        dp = [float(inf)]*(n+1)

        dp[0] = 0 

        for i in range(1,n+1):
            freq = {}

            for j in range(i-1,-1,-1):
                freq[s[j]] = freq.get(s[j],0)+1
                if len(set(freq.values()))==1:
                    dp[i] = min(dp[i], dp[j]+1)


        return dp[n]
        