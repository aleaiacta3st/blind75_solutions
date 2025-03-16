class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(1,n+1):
            for j in range(0,i):
                if dp[j]==True:
                    if s[j:i] in wordDict:
                        dp[i]=True
        return dp[n]

# Create an array of Booleans
# subproblem: dp[i] represents whether the substring s[0:i] can be segmented
# dp[0] is about s[0:0] which is the empty string =0 
# when you are at i, look behind you for break points
# the break points have their value set to true in the dp array 
# for every break point with value = True, 
#     check if the substring between j and i is a part of the dictionary
# if the substring[j:i] is a part of substring 
#     then i is a breaking point and set dp[i] = True 
# we need the value of dp[n]   


# In Python slicing notation s[start:end]:
# The start index is inclusive
# The end index is exclusive
# So:
# s[0:1] contains only the character at index 0 (first character)
# s[0:2] contains characters at indices 0 and 1 (first two characters)
# s[0:3] contains characters at indices 0, 1, and 2 (first three characters)

# dp[i] represents whether the substring s[0:i] can be segmented
# Due to Python's slicing behavior, s[0:i] includes characters '
# 'from index 0 up to but NOT including index i'
# so dp[n] represents whether the string s[0:n] can be segmented
# which is nothing but the whole string
# dp[0] is about s[0:0] which is the empty string and it can always be segemented.

# Outer Loop: for i in range(1, n+1)
# This isn't directly iterating over the string characters - '
# 'it's iterating over ending positions:
# When i=1, we're asking about s[0:1]
# When i=2, we're asking about s[0:2]
# When i=n, we're asking about s[0:n] (the whole string)'
# if you use range(0,n), you talk about s[0:n-1] - this does not include the last element
# there is one more element after this.
        