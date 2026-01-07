class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r  # bounds after over-expansion
    
        start, end = 0, 0
        for i in range(len(s)):
            l1, r1 = expand(i, i)      # odd
            l2, r2 = expand(i, i + 1)  # even
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2
        return s[start:end]

# def expand_around_centre(x,y)
# a helper function which takes two arguments, the indices where left and right initially start and returns the max size of palindrome around that center 
# the center for a palindrome 
#     if odd, there is just one center and the palin expands from there 
#     if even, between chars at i and i+1
# the helper func is the same regardless of the length of the palin 
# while assuming an odd sized palin, set left=right=i 
# while assuming an even sized palin, left =i, right =i+1
# observe that the starting position of the palin is not left but left+1
# this is because left and right move apart one final time before the palin condition breaks 
# these final left and right are not the bounds of the palin 
# the bounds are the previous indices 
# so move left one position forward 

# in the main function, consider cases of both odd sized and even sized palin 
# take the greatest of them and compare them to the greatest so far 
# update start with appropriate index 
    
# In the main func, when i is n-1, i+1 would be n. right=n 
# but there is no index n in the string 
# but the while condition in helper function fails and we never update the start position with this illegal index as max size is 0
# you can add a check to prevent this from happening. but I didnt in my code because it makes no difference 
# the helper func is preventing from issues

# The time complexity of your solution is O(n²), where n is the length of the input string.
# Here's the breakdown:

# You have a main loop that iterates through each character of the string, which runs in O(n) time.
# For each character, you call the expand_around_centre function twice (once for odd-length palindromes and once for even-length palindromes).
# The expand_around_centre function itself can, in the worst case, expand to check the entire string. This happens for cases like "aaaaa" where every character is the same. Each call to this function therefore has a worst-case time complexity of O(n).
# Combining these, you have O(n) iterations of the main loop, each doing O(n) work, resulting in an overall time complexity of O(n²).
