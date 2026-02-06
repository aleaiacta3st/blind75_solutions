class Solution:
    def reverse(self, x: int) -> int:

        result=0 

        sign=1 if x>=0 else -1

        x=abs(x)


        while x!=0:
            if result>((2**31-1)//10):
                return 0
            result=result*10
            result=result+(x%10)
            x=x//10

        return result*sign
        