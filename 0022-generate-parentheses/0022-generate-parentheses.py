class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result=[]

        def backtrack(open_count,close_count,combo):
            if len(combo)==2*n:
                result.append(combo)
                return
            if close_count<open_count:
                
                backtrack(open_count,close_count+1,combo+")")
            if open_count<n:
                
                backtrack(open_count+1,close_count,combo+"(")



        backtrack(0,0,"")

        return result

            



