class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        def expand_around_centre(x,y):
            left=x 
            right=y
            count=0
            while left>=0 and right<=n-1:
                if s[left]==s[right]:#first check if initial positions are equal
                    count+=1
                    left=left-1
                    right=right+1
                else:
                    return count #when chars do not match return count seen so far
            return count #still returns count should the while loop fail
        
        count=0
        for i in range(n):
            count_odd = expand_around_centre(i,i)
            count_even = expand_around_centre(i,i+1)
            count=count+count_odd+count_even
        return count

#adapted from longest palindrome solution
        