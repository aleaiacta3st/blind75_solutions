class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []


        def dfs(start, combo, remaining):
            if remaining==0:
                result.append(combo[:])
                return
            if remaining<0:
                return 


            for i in range(start,len(candidates)):
                combo.append(candidates[i])
                dfs(i, combo, remaining-candidates[i])
                combo.pop()


        dfs(0,[], target)

        return result
        