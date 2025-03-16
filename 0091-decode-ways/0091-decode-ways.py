class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp=[0]*(n)
        if (s=='0'):
            return 0
        if (n==0):
            return 0
        if (n==1):
            return 1
        
        dp[0]=1
        
        if s[0]=='0' and s[1]=='0': #00 eliminated
            return 0
        
        if s[0]=='0' and s[1]!='0': #01,02,03,...,09 eliminated
            return 0

        if s[0]!='0' and s[1]=='0':  #10,20 allowed. 30,40,50,...,90 eliminated
            if s[0]=='1' or s[0]=='2':
                dp[1]=1
            else:
                return 0

        if s[0]!='0' and s[1]!='0': #if the first two digits together are in range 1-26, 
                                    #then they can be interpreted in 2 ways. 
                                    # 26 can be decoded as bf or z (2 ways)
                                    #42 can only be interpreted as db (1 way)
            if '10'<s[0:2]<='26':
                dp[1]=2
            else:
                dp[1]=1

        
        for i in range(2,n):
            if s[i-1]=='0' and s[i]=='0':
                return 0

            if s[i-1]=='0' and s[i]!='0':
                dp[i]=dp[i-1] 

            if s[i-1]!='0' and s[i]=='0':
                if s[i-1]=='1' or s[i-1]=='2':
                    dp[i]=dp[i-2]
                else:
                    return 0

            if s[i-1]!='0' and s[i]!='0':
                if '10' < s[i-1:i+1] <= '26':
                    dp[i] = dp[i-1]+dp[i-2]
                else:
                    dp[i]=dp[i-1]
        return dp[n-1]
    


# dp[i] is the number of ways the substring s[0:i+1] can be decoded

# if s[i-1]=='0' and s[i]=='0':
#             return 0
# 0 cannot stand on its own. it has to pair with 1 or 2 to be useful. 
# In this case 0 is paired with 0. This cannot be decoded. 


# if s[i-1]=='0' and s[i]!='0':
#             dp[i]=dp[i-1]
# These are numbers like 01,02,03,04,05,...,09
# we have 0 in the i-1 position
# Can i pair with i-1 and form a valid number that can de decoded?
# No. If it pairs we get numbers like 01,02,03 which carry no meaning.
# Hence i cannot pair with i-1.
# dp[i]=dp[i-1]
# suppose the substring ending 1 step before the current substring can be decoded in 3 ways.
# Assume 22456 can be decoded as 
# abcdf
# bgf
# mklo 
# In this case, we concluded that a pairing is not possible.
# If the ith element is 7, the new string to be decoded becomes 224567. Let 7=z 
# This new string can be decoded as 
# abcdfz
# bgfz
# mkloz
# That is why dp[i]=dp[i-1]

# if s[i-1]!='0' and s[i]=='0':
#             if s[i-1]=='1' or s[i-1]=='2':
#                 dp[i]=dp[i-2]
#             else:
#                 return 0
# numbers under consideration are 10,20,30,40,...,90
# 0 in the ith position HAS to pair with either 1 or 2 in the i-1 position 
# dp[i]=dp[i-2]
# dp[i-2]=567
# dp[i-1]=5671
# dp[i]=56710
# suppose dp[i-2] 567 can be decoded in 2 ways 
# abc 
# def 
# 56710 decodes to 567 and 10. assume 10 decodes to g. 
# 567 now can be decoded in 2 ways 
# abcg 
# defg 
# In this case dp[i] is not dependent on dp[i-1]
# 30,40,50 are invalid 
# 0 cannot stand on its own. So it has to pair up. But with only 1 or 2.
# We have considered those cases above
# If i-1 is not 1 or 2 when i=0, then the sequence is invalid and cannot be decoded. 

# if s[i-1]!='0' and s[i]!='0':
#             if '10' < s[i-1:i+1] <= '26':
#                 dp[i] = dp[i-1]+dp[i-2]
#             else:
#                 dp[i]=dp[i-1]
# The last case where neither i nor i-1 are 0s 
# So we are considering numbers like 12,24,78,87 etc
# if this two digit number is in the range 10,26
# dp[i] = dp[i-1]+dp[i-2]
# dp[i] =2311
# dp[i-1] = 231
# dp[i-2] = 23
# dp[i-2] can be decoded in 3 ways
# hji 
# lomh
# bhy 
# dp[i-1] can be decoded in 4 ways
# pith 
# fgtya
# ert 
# mlpq 
# The ith character 1 can stand on its own and decode to v 
# or it can pair up the char at i-1 position and decode to x
# Consider the case where it stands on its own and does not pair 
# dp[i-1], 231, decoded to 
# pith 
# fgtya
# ert 
# mlpq 
# Now dp[i], 2311 decodes to (i is standing on its own)
# pithv
# fgtyav
# ertv 
# mlpqv 
# Consider the case where it pairs with i-1 and decodes to x
# dp[i] is 2311 and i has paired with i-1
# so the coded message is 23 11
# 23(dp(i-2)) was decoded as 
# hji 
# lomh
# bhy 
# 23 11 will be decoded as 
# hjix
# lomhx
# bhyx
# so dp[i] can de decoded as the following 
# pithv (no pairing)
# fgtyav (no pairing)
# ertv (no pairing)
# mlpqv (no pairing)
# hjix (pairing)
# lomhx (pairing)
# bhyx (pairing)
        