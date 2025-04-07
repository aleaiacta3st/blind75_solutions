class Solution:
    class Trie:
        def __init__(self):
            self.children={}
            self.is_end_of_word=False
            self.word=None

        def insert(self, word: str) -> None:
            current = self
            for letter in word:
                if letter not in current.children:
                    current.children[letter] = Solution.Trie()  # Use Solution.Trie instead of Trie
                current = current.children[letter]
            current.is_end_of_word = True 
            current.word = word

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        final = set()  # You defined this as a set
        visited = set()

        word_trie = Solution.Trie()  # Use Solution.Trie instead of Trie
        for word in words:
            word_trie.insert(word)

        def backtrack(x, y, current):
            if board[x][y] not in current.children:
                return False 
            current = current.children[board[x][y]]
            if current.is_end_of_word:
                final.add(current.word)  # Use add for sets, not append
                current.is_end_of_word = False
            visited.add((x, y))
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in directions:
                nx = x + dx 
                ny = y + dy 
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    backtrack(nx, ny, current)
            visited.remove((x, y))
            return False
        
        for i in range(m):
            for j in range(n):
                backtrack(i, j, word_trie)  # Pass word_trie, not current
                
        return list(final)  # Convert set to list before returning

# Understanding Multiple Trie Nodes for the Same Letter
# question was about whether marking a word as "found" (by setting is_end_of_word = False) could cause problems for other words that end with the same letter.
# The key insight is that in a Trie:
# Each letter in each unique path gets its own node. For words like "cat", "rat", and "bat":

# They follow completely different paths from the root
# Each has its own separate 't' node at the end
# These 't' nodes are independent of each other

# Even though all three words end with 't', there are three distinct 't' nodes in the Trie, each with:

# Its own is_end_of_word flag
# Its own word attribute

# This is why we can safely mark a word as "found" by setting current.is_end_of_word = False - it only affects that specific word's end node, not any other word that happens to share that letter.
# The Trie's structure efficiently represents all words while maintaining the independence of each word path.


    







# if word in words are oat and oath, in no trie approach you search for oa in oat search, and then oa again in oath search. but in trie that is not needed.

# There is no link between the board and the trie structure you created. trie is created from the words list.

# THINK OF EACH WORD AS A PATH 

# The root node typically has is_end_of_word = False.
# Let me clarify about nodes and the is_end_of_word property:

# Each node represents a character in a path
# A node's is_end_of_word property indicates if the path from root to THIS node forms a complete word
# This property belongs to the node itself, not to any of its children

# For example, with words ["CAT", "CAR"]:

# The 'C' node has children {'A': NodeA}
# The 'A' node has children {'T': NodeT, 'R': NodeR}
# Both NodeT and NodeR would have is_end_of_word = True
# But 'C' and 'A' nodes would have is_end_of_word = False (unless "C" or "CA" were also words in our list)

# The is_end_of_word property tells us "is the string formed by following the path to this node a complete word?" - it doesn't depend on the node's children.


# #                   Root
# #                 is_end = False
# #                 children = {'C': Node_C}
# #                       |
# #                       V
# #                     Node_C
# #                 is_end = False
# #                 children = {'A': Node_A}
# #                       |
# #                       V
# #                     Node_A
# #                 is_end = False 
# #                 children = {'T': Node_T, 'R': Node_R}
# #                     /           \
# #                    /             \
# #                   V               V
# #                Node_T          Node_R
# #             is_end = True    is_end = True
# #             word = "CAT"     word = "CAR"
# #             children = {}    children = {}


# Key points:

# # Each node represents a letter in a path
# # The node's is_end_of_word flag indicates if the path to this node forms a complete word
# # A node's children dictionary contains all possible next letters
# # The root node doesn't represent any letter - it's just the starting point
# # When we check current.is_end_of_word, we're checking if the path so far forms a word


# Your question:
# In a trie, each node represents a letter. If we insert two words like "cat" and "bat", which both end in the letter 't', will they share the same 't' node?

# Answer:
# No, they will not share the same 't' node unless they have the same prefix.

# "cat" inserts the path: 'c' → 'a' → 't'

# "bat" inserts the path: 'b' → 'a' → 't'

# Since 'c' and 'b' are different starting points, their entire paths are separate — including their own versions of 'a' and 't'.

# Only words that share the exact prefix (like "car" and "cart") will share nodes along that common prefix path.

# So the trie branches at the point where the words differ. That's how it efficiently compresses shared prefixes without mixing unrelated paths.

# car 
# cars 
# if we set the is end value of r, car will not be detected again but cars will be 

# bat 
# cat 
# these t nodes are completely different. if you set one of is end value of a t to be False, it is not going to affect the other


# The optimization current.is_end_of_word = False # Mark as found prevents the same word from being found multiple times on the board.
# Without this step, here's what could happen:

# The word "CAT" exists at multiple positions on the board (e.g., starting at (0,0) and starting at (2,3))
# When backtracking from position (0,0), we find "CAT" and add it to our results list
# When backtracking from position (2,3), we find "CAT" again and add it to our results list again
# Our final result would have duplicate entries of "CAT"

# By setting current.is_end_of_word = False after finding a word, we're effectively marking that specific word as "already found" in the Trie.
# When we encounter that same word again during backtracking from a different starting position, the is_end_of_word flag will be False, so we won't add it to our results again.
# This works because each word has its own unique endpoint node in the Trie (as we discussed with words like "cat", "rat", "bat" each having their own 't' node), so marking one word as found doesn't affect our ability to find other words.

# Summary: Word Search II Trie Implementation Issues
# The main issues in your original solution were:

# Nested Class References: When defining Trie as a nested class inside Solution, you must use Solution.Trie() instead of just Trie() when creating new instances. This caused the NameError.
# Starting Point for Each Board Position: You assigned current = word_trie and then passed current to each backtracking call. This is problematic because:

# We need to start from the root of the Trie for each new position on the board
# current gets modified during backtracking with current = current.children[board[x][y]]
# Subsequent board positions wouldn't be starting from the Trie root


# Set vs List Operations: You defined final as a set but used list methods (append). When working with sets, use add() instead, and convert back to list before returning.

# By fixing these issues, each cell on the board gets a proper chance to be the starting point for any word in our dictionary, which is essential for the algorithm to work correctly.