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
        