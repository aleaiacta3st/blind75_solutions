class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*(len(nums)+1)
        for i in range(len(nums)-2,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)

    # dp[i] is "length of longest increasing subsequence starting at position i"
    # so consider the array nums[i:] as the subproblem
    # we need to find the relationship between subproblems
    # consider the ith element
    # consider array nums[i+1:]
    # when will i be a part of the longest increasing subsequence
    # for every j>i, i can form a part of the sequence
    #then dp[i] = 1(the ith element) + dp[j]
    # there are many j>i
    # we need to calculate 1+dp[j] for all such j and take the maximum

    # in coinchange we returned dp[n]? Here we returned max(dp). why?
    #what we return depends on how we define our subproblems and what the question asks
    #Coin change
    #   The problem asks for a specific target (making amount n)
    #   dp[i] = "minimum coins needed to make amount i"
    #   The answer must be dp[n] because we need exactly amount n
    # Longest Increasing Subsequence:
    #   The problem asks for the longest subsequence 
    #       anywhere in the array
    #   dp[i] = "length of LIS starting at position i"
    #   The LIS could start at any position, so we must 
    #       check all possibilities with max(dp)

    # the relationship between our DP definition and what we 
    # return depends on whether:
    #   The problem has a specific target state (return dp[target])
    #   The problem asks for the best result among all states 
    #       (return max(dp) or min(dp))

    #what we initialize dp to 0,1,inf or -inf also depends on the problem
    #every number can form a sequence by itself. therefore minimum lis=1. 
    # that is what we have initialised dp to.

    #Minimization problems → initialize to float('inf')
    #Maximization problems → initialize to -float('inf')
        