class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        def expand(l,r):
            while l>=0 and r<n and s[l]==s[r]:
                l=l-1
                r=r+1
            return (l+1,r)


        start=0
        end=0

        for i in range(n):
            l1,r1=expand(i,i)
            l2,r2=expand(i,i+1)

            if r1-l1>end-start:
                start=l1
                end=r1

            if r2-l2>end-start:
                start=l2
                end=r2 


        return s[start:end]
        