class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        def expand_around_centre(x,y):
            left=x 
            right=y
            max_size=0 
            while left>=0 and right<=n-1:
                if s[left]==s[right]:#first check if initial positions are equal
                    current_size=right-left+1
                    if current_size>max_size:
                        max_size=current_size
                    left=left-1
                    right=right+1
                else:
                    return (max_size,left+1) #when chars do not match return the max size seen so far
            return (max_size,left+1) #still returns the max size should the while loop fail
        
        greatest_size=0
        start=0
        for i in range(n):
            odd_size,odd_start = expand_around_centre(i,i)
            even_size,even_start = expand_around_centre(i,i+1)
            if odd_size> even_size:
                if odd_size>greatest_size:
                    greatest_size=odd_size
                    start=odd_start
            else: 
                if even_size>greatest_size:
                    greatest_size=even_size
                    start=even_start
        return s[start:start+greatest_size]