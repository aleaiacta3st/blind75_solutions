class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        visited=set()

        def dfs(x,y,index):
            if board[x][y] != word[index]:
                return False
            visited.add((x,y))
            index+=1
            if index == len(word):
                return True
            directions = [(-1, 0),  # up (x-1, y)
                            (1, 0),   # down (x+1, y)
                            (0, -1),  # left (x, y-1)
                            (0, 1)    # right (x, y+1)
                            ]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    if dfs(nx, ny, index):
                        return True
            visited.remove((x, y))
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    if dfs(i,j,0):
                        return True               
        return False
        


# Think of this algorithm as a journey through a labyrinth where each correct letter is a checkpoint. When you reach a checkpoint (match a letter), you must immediately ask: "Have I completed my quest?"


# explain why in graphs we did not need to delete from set. its been some time since i solved a graph problem. the general graph problem which does not require us delete elements rfom the visited set,
# THE CORE DIFFERENCE: One Path vs. All Paths
# \U0001f537 In graph traversal (DFS/BFS):
# Your goal is usually to visit every node once.
# You don't care about trying every possible path from A to B.
# You mark a node as visited once, and that's it.
# Once it's visited, revisiting it is never useful.
# Common use cases:
# Is there a path from X to Y?
# What are all connected components?
# Is the graph bipartite?
# Count nodes, detect cycles, etc.

# \U0001f501 So, in those problems:
# visited = set()

# def dfs(node):
#     visited.add(node)
#     for neighbor in graph[node]:
#         if neighbor not in visited:
#             dfs(neighbor)

# No backtracking. No removal.
# Why? Because we never need to try another path using that node. We're not tracking specific routes, just coverage.
# BUT... Word Search is not that.
# \U0001f9e0 Word Search ≠ Simple Graph DFS
# Word Search is about:

# Trying every possible path that might spell the exact sequence.

# Each recursive DFS call is a different attempt to form the word.

# So if you visit a cell on one path and mark it visited, you must undo that visit (backtrack) after that path fails. Because:

# That cell might be valid for another path from a different direction.
    

# Graph Traversal vs. Word Search: The Backtracking Difference
# In standard graph problems, we typically use a visited set to avoid cycles and prevent infinite loops. Once we mark a node as visited, we generally keep it that way throughout the entire traversal. This approach works well for:

# Finding if a path exists between two nodes
# Counting connected components
# Topological sorting
# Detecting cycles

# Why Word Search Is Different
# Word Search requires backtracking (removing elements from the visited set) for several critical reasons:

# Specific Character Sequence: Unlike general graph traversal where you're looking for any valid path, Word Search requires finding a specific sequence of characters in a particular order.
# Path Exclusivity: In Word Search, a cell can only be used ONCE in a single word. The visited set prevents reusing a cell within the SAME path attempt.
# Multiple Valid Paths: The key insight is that a cell that doesn't work for one path attempt might be CRUCIAL for another valid path from a different direction or starting point.

# Graph DFS doesn’t “undo” steps; it just moves forward or stops.
# Example: In DFS on a graph to check if a path exists from A to Z, you mark A as visited, move to B, mark it, and so on. If B leads nowhere, you don’t unmark it—you just try another node from A. The set persists because revisiting B is pointless.

# Why Backtrack Here?
# In a word-search maze:

# You reuse letters across different paths (unlike graphs, where nodes are visited once).
# If “CAT” fails at “T”, you backtrack from T, unmark it, and try “CAP”—same starting letter, different path.
# Without erasing steps, you’d block valid alternative paths, assuming letters are “used up.”
# Key Difference
# Graphs: Visited set is permanent—no need to revisit or retry paths.
# Backtracking: Steps are temporary—undoing lets you explore all possibilities systematically.

# Consistency in Function Design: The DFS function is designed to verify whether a path starting at position (i,j) matches the substring of the word beginning at position index. For the first call, that's the entire word, so we start at index 0.
# General Pattern Recognition: The DFS function should handle any substring of the word, not just "everything except the first character." This makes the logic more uniform and easier to understand.
# Verification Inside DFS: Even though we might check the first character match in the main loop, a well-designed DFS function would still verify the match at its current position as its first operation:


# The base case if index == len(word): return True works because:
# In zero-indexed languages like Python, valid indices for a string of length n run from 0 to n-1.
# When your index reaches len(word), it means:

# You've already successfully matched all characters from indices 0 to len(word)-1
# There are no more characters left to match
# Your path has successfully traced the entire word!


# Why Add to the visited Set?
# Purpose: The visited set tracks which cells we’ve used in our current path.
# Reason: In a word search, you can’t reuse the same cell twice in one path (no doubling back to the same spot). When we visit a cell—like (x, y)—we add it to visited to mark it as "taken" for this attempt.
# In the Code: After checking board[x][y] == word[index], we do visited.add((x, y)). This says, "We’re using this cell now, so don’t revisit it while exploring this path."

# Why Remove from the visited Set?
# Purpose: Removing a cell from visited happens when we backtrack, undoing our choice so the cell can be used in a different path.
# Reason: If a path fails (e.g., we can’t find the next letter), we need to try other options. By removing the cell with visited.remove((x, y)), we free it up for other attempts, either from the same starting point or a different one later.
# In the Code: After trying all directions from (x, y) and failing (no True returned), we remove (x, y) from visited. This "resets" it for other possibilities.

# How It Works Together (Backtracking 101)
# Trying a Path:
# Start at a cell, check if it matches the current letter.
# Add it to visited.
# Move to the next letter (index += 1) and try adjacent cells (up, down, left, right).
# If all letters match (index == len(word)), return True.
# Backtracking:
# If no direction works (dead end), remove the current cell from visited and return False.
# This lets the code back up to the previous step and try a different direction.

# Key Takeaway
# Add: Locks a cell into the current path.
# Remove: Unlocks it when the path fails, so other paths can use it.
# Backtracking: It’s like exploring a maze—mark your steps, and if you hit a dead end, erase the mark and try another way.