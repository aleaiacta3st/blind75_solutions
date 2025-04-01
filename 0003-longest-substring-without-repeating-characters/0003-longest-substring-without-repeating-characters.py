class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None:
            return 0
        longest = 0 
        n=len(s)
        visited={}
        left=0
        for i in range(n):
            if s[i] not in visited:
                visited[s[i]]=i 
                longest = max(longest,i-left+1)
            else:
                if visited[s[i]]>=left:
                    left=visited[s[i]]+1
                visited[s[i]]=i
                longest = max(longest,i-left+1)
        return longest


# why right-left +1
# For example, if left = 2 and right = 5:

# Characters at indices 2, 3, 4, and 5 are included in your substring
# That's 4 characters total
# And indeed, 5-2+1 = 4

# This is different from calculating a simple difference which would give you 
# (5-2 = 3), missing one character.
# It's similar to calculating how many integers exist between two numbers '
# '(inclusive) - the formula is always end - start + 1.'

# The core logic:

# Use a sliding window with left pointer at start of current valid substring
# Track character positions in a dictionary
# When finding a duplicate character, update left pointer only if the previous 
# occurrence is within current window
# Calculate window length at each step and track maximum

# The key condition for updating left:

# When we find a character we've seen before
# AND its previous position ≥ current left
# Then move left to (previous position + 1)

# This approach ensures we always maintain a window with unique characters, 
# efficiently jumping the left pointer forward when needed rather than checking 
# character by character.
        