class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        n=len(digits) 

        phone={
            '2':'abc', 
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz',
            }

        result=[]

        def backtrack(i,path):
            if i==len(digits):
                result.append("".join(path))
                return 
            for ch in phone[digits[i]]:
                path.append(ch)
                backtrack(i+1,path)
                path.pop() 

        backtrack(0,[])

        return result

        
            



        