class Solution:
    def isPalindrome(self, x: int) -> bool:



        x=str(x)
        n=len(x)

        left=0
        right=n-1

        while left<right:
            if not x[left]==x[right]:
                return False
            else:
                left=left+1
                right=right-1

        return True
        