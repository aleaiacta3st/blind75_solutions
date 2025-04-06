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





# If a recursive call has ended, it has hit one of the 3 base cases. It has either added a combination or we found the last number that was added to our combination is unfit. Either way we have to pop it off to search for more sequences.
    
# As a reminder, backtracking is a general algorithm for finding all (or some) solutions to some computational problems. The idea is that it incrementally builds candidates to the solutions, and abandons a candidate ("backtrack") as soon as it determines that this candidate cannot lead to a final solution.

# Specifically, to our problem, we could incrementally build the combination, and once we find the current combination is not valid, we backtrack and try another option.

# return current_list.append(num)
# append() in Python modifies the list in-place and returns None - it doesn't return the modified list.
# When you write return current_list.append(num), you're actually returning None to the caller, not the updated list you intended. This is why your function isn't building combinations properly.
# This is a common mistake in Python. List methods like append(), extend(), and sort() all modify the list in-place and return None. This is different from methods like + or slicing, which create new lists.
# To fix this specific line, you'd need to:
# current_list.append(num)
# return current_list
# \
# Yes, lists can be passed as arguments in Python, and this is where a key concept comes into play.
# In Python, when you pass a list to a function:

# The function receives a reference to the same list object, not a copy
# Any modifications to the list inside the function affect the original list
# This is true for all mutable objects (lists, dictionaries, sets, etc.)
# For backtracking algorithms like Combination Sum, this shared reference behavior is actually useful. You can:

# Add an element to your combination
# Make recursive calls (which will see the updated list)
# Remove the element when backtracking

# This is why many backtracking solutions use code patterns like:
# current.append(num)  # Add element
# backtrack(...)       # Recurse with the modified list
# current.pop()        # Remove element (backtrack)
# The shared reference allows the parent function to see changes made by child calls, which is perfect for building and exploring different combinations.RetryST
    

# if we do not have a visited set, if we see the array given to us as a graph, where a number is connected too every otger number, how to prevent getting stuck in cyclkes
# To explain how we prevent cycles without a visited set in the Combination Sum problem:
# The key insight is that we're always decreasing the target value with each recursive call. Since all the candidate numbers are positive (as per the problem constraints), each time we include a number in our combination, we reduce the remaining target.
# This means:

# If we choose any number, the target decreases
# Eventually, we either reach target = 0 (a valid combination) or target < 0 (invalid path)
# This guarantees termination without cycles
# In a graph analogy, we're not actually traversing a cyclic graph - we're traversing a DAG (Directed Acyclic Graph) because each choice leads us strictly "downward" toward zero. There's no way to form a cycle because we can't increase the target value.
# This is why we don't need a visited set for this specific problem - the decreasing target value inherently prevents infinite loops.

# The DAG (Directed Acyclic Graph) analogy is illuminating for understanding why we don't need a visited set in the Combination Sum problem.
# In graph algorithms, we typically use a visited set to avoid processing the same node multiple times and prevent infinite loops when there are cycles. However, in the Combination Sum problem, the structure naturally prevents cycles.
# Here's why:

# Every time we select a number from our candidates, we subtract it from our target
# Since all numbers in the candidates array are positive (per the problem constraints), each step decreases our remaining target
# This creates a one-directional flow - we're always moving "downward" toward zero

# This is exactly what a DAG is - a graph where all edges point in a consistent direction with no way to form a cycle. Think of each state as (current_combination, remaining_target). Every edge leads to a state with a smaller remaining target, making it impossible to return to a previously visited state.
# It's like descending a staircase - you can only go down, never up, so you can't possibly get stuck in a loop.
# This is why a visited set is unnecessary for this specific problem - the mathematical constraint of positive integers and decreasing target values prevents cycles automatically.
    
# You only look at the current index and forward (never backward), which prevents duplicate combinations
# The key insight here addresses how we prevent duplicate combinations while still allowing unlimited reuse of each number.
# Let me explain with an example using candidates [2, 3, 6, 7] and target = 7:
# If we allowed ourselves to select numbers in any order (looking backward), we could generate:

# [2, 2, 3] (starting with 2, then 2 again, then 3)
# [3, 2, 2] (starting with 3, then 2 twice)
# These contain exactly the same numbers (two 2's and one 3), so they're considered the same combination - just arranged differently.
# By only looking from the current index forward:

# When we start with 2, we only consider [2, 3, 6, 7] for future selections
# When we start with 3, we only consider [3, 6, 7] for future selections (never going back to 2)
# This forces our combinations to be built in a specific order (non-decreasing), ensuring we only generate each unique combination once.  

# in the word search problem of leetocde, why did we use a visited set? i am not sure but also was there a main outer for loop unlike this combination sum problem? why?
# Why a visited set in Word Search?
# In Word Search, you have a 2D board and need to prevent revisiting the same cell within a single word path. The visited set (or matrix) prevents infinite loops by marking cells you've already used in your current path. Without it, you could end up in scenarios where your search bounces back and forth between adjacent cells indefinitely.
# Why outer loops in Word Search but not in Combination Sum?
# Word Search requires outer loops because:

# The word could start from ANY cell in the grid
# You need to try each cell as a potential starting point
# Example structure of Word Search:
# # Outer loops to try each starting position
# for i in range(rows):
#     for j in range(cols):
#         if dfs(board, i, j, word, 0):  # Try DFS from this cell
#             return True
# In Combination Sum, we don't need separate searches from each candidate because:

# We're looking at all possible combinations from the entire array
# Using a start index parameter ensures we consider all combinations without duplication
# A single call with start index 0 explores all possible paths

# The fundamental difference is that Word Search is about finding a specific path on a grid with positional constraints, while Combination Sum is about finding combinations from a set where order doesn't matter and (potentially) reuse is allowed.

# how can a recursive function not return anything? if it wont return anything, how will its parent function finish its eecution and get popped out of the stack

# The backtracking function technically does return - it just doesn't return the combinations themselves. Instead, it returns control flow (like with return statements when hitting base cases).

# The function "returns" in the sense that it stops execution and passes control back to the previous recursive call. This allows the algorithm to backtrack and try different paths.
# Multiple combinations are built because the algorithm tries different starting numbers and different paths from each starting point. When it finds a valid combination, it records it and backtracks to try other possibilities.

# This is a backtracking algorithm that:

# Builds combos by adding candidates one-by-one.

# Recurses with the reduced target.

# Allows reuse of the same number by calling backtrack(..., i) instead of i+1.

# Backtracks (removes last added number) after each call to explore other paths.

# How multiple combos are built:
# Each time the target hits 0, a copy of the current path is added to final_list. The function then "backtracks" — removes the last added number — and tries the next option.

# Why no infinite loops:
# The remaining target shrinks every time a number is added.

# If the target goes below zero, recursion stops.

# Hence, even if we reuse the same number, we can’t loop forever — the base case cuts off the cycle

# In this problem, here’s what you are trusting recursion to do:
# You trust that for any current state — with:

# a remaining_target,

# a current_combo_being_built,

# and a starting_index...

# ...the recursive function will:
# ✅ Explore every valid combination from that point onward
# ✅ Add to the result only if the combo sums exactly to the target
# ✅ Automatically stop exploring when the sum exceeds the target
# ✅ Backtrack properly after each attempt, cleaning up the path for the next try

# In other words:
# You focus only on this level:
# “I’ll pick a number, try it, and trust my deeper call to explore everything that happens after choosing this number.”

# You don’t need to worry about:

# What happens 3 levels deeper.

# How many combinations exist.

# Whether the backtrack works — it does, because you pop after each call.
# \U0001f9ec Summary:
# Trust that recursion explores every future from the current choice.
# Trust that the base cases protect you from overstepping.
# Trust that backtracking keeps the path clean for the next decision.

# That's what “trust the recursion” means.
# The recursive call is your army — you give the command, they explore all consequences.

# You are the general. Let them fight.





        