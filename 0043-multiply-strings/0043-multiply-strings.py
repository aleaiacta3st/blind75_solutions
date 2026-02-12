class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        m=len(num1)
        n=len(num2)

        result=[0]*(m+n)

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                d1=int(num1[i])
                d2=int(num2[j])
                mul=d1*d2
                total=result[i+j+1]+mul
                result[i+j+1]=total%10
                result[i+j]+=total//10 


        result = "".join(map(str,result))

        i=0
        while i<(m+n-1) and result[i]=='0':
            i=i+1


        return result[i:]
        