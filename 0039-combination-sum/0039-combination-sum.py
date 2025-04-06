class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        candidates.sort()  # Optional but helps with optimization
        final_list=[]
        def backtrack(remaining_target,current_combo_being_built,starting_index):
            if remaining_target==0:
                final_list.append(current_combo_being_built[:])
                return
            if remaining_target<0:
                return #prevents unnecessary recursion
            if candidates[starting_index]>remaining_target:
                return 
            for i in range(starting_index, n):
                # Add this candidate to your combination
                current_combo_being_built.append(candidates[i])
                
                # Explore this path through recursion
                backtrack(remaining_target - candidates[i], current_combo_being_built, i)  # Note: i not i+1 if we can reuse!
                
                # CRITICAL: Remove this candidate (backtrack) before trying the next one
                current_combo_being_built.pop()

        backtrack(target,[],0)
        return final_list
        