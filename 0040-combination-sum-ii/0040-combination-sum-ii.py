class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:


        n=len(candidates)

        candidates.sort()

        result=[]


        def backtrack(start,combo,remaining):
            if remaining==0:
                result.append(combo[:])
                return
            if remaining<0:
                return 
            for i in range(start,n):
                if candidates[i]>remaining:
                    break
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                combo.append(candidates[i])
                backtrack(i+1,combo,remaining-candidates[i])
                combo.pop()

        backtrack(0,[],target)

        return result

        