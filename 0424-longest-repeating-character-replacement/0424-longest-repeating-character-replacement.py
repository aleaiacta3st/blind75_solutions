class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency_tracker = {}
        left=0
        n=len(s)
        max_frequency=0
        longest=0
        for i in range(n):
            if s[i] not in frequency_tracker:
                frequency_tracker[s[i]]=1 
            else:
                frequency_tracker[s[i]]+=1
            max_frequency=max(max_frequency,frequency_tracker[s[i]])
            while (i-left+1)-max_frequency > k:
                frequency_tracker[s[left]]-=1
                left+=1
            longest=max(longest,i-left+1)
        return longest
        