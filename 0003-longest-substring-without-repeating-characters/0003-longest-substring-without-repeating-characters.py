class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_length=0

        left=0

        dict={}

        for right,char in enumerate(s):
            if char in dict and dict[char]>=left:
                left=dict[char]+1
            dict[char]=right
            max_length=max(max_length, right-left+1)

        return max_length
        