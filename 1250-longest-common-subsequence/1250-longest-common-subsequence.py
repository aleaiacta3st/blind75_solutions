class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2) 
        dp =[[0]*(n+1) for _ in range(m+1)]
        #has n+1 columns and m+1 rows

        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[m][n]


    # loop indexing issues
    # extra column and row for empty strings in the dp table. be mindful of them. 
    # we want to fill the dp table so i should run till i=m and j till j=n
    # why is minimum range 1? If you use 0, dp[i-1] and dp[j-1] will be come illegal
    # And anyway all dp values with either i or j = 0 are already set to 0. 
    # we want to fill the dp table and we also want to make correct comparison of 
    # characters from text1 and text2
    # compare values at i-1 and j-1 but update value at dp[i][j]. 
    # this is because of the row and column of empty strings 

    # prefixes 
    # compare the ending character
    # if they match we extend the sequence by the current character which is text1[i]=text2[j]
    # dp[i][j]=1+dp[i-1][j-1]
    # if they do not match, we cannot extend the sequence and the length cannot increase
    # so it should take on the value of something that has been previously calculated
    # if you consider the example of abcde and ace
    # abcd, ac subproblem can only have come from abc,ac and abcd,a subproblems
    # pick whatever is the maximum
    # dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    # both characters at i and j cannot be a part of the sequence 
    # choose i, exclude j
    # choose j, exclude i 
    # when these last characters do not match, we cannot extend both the sequences 
    # simultaneously like we did when they matched
    # When we use max(dp[i-1][j], dp[i][j-1]), we're not extending anything. '
    # 'We're selecting which previously calculated value to use.
    # By taking the maximum, we're choosing the longer of those two previously '
    # 'calculated subsequence lengths. No new character is being added in this step '
    # '- we're just selecting which existing solution to carry forward.
    # dp table has an extra row and column for empty strings 
    # first row and column of the table will be 0
    # should be filled row by row, left to right 

    # remember we increment the subproblems by 1. no big or arbitrary jumps
        