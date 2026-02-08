class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        

        n=len(candidates)

        result=[]

        def backtrack(start,combo,remaining):
            if remaining==0:
                result.append(combo[:])
                return 
            if remaining<0:
                return 

            for i in range(start,n):
                combo.append(candidates[i])
                backtrack(i,combo,remaining-candidates[i])
                combo.pop()


        backtrack(0,[],target)

        return result
