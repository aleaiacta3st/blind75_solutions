class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        char_freq={}

        for c in s:
            char_freq[c]=char_freq.get(c,0)+1


        for c in t:
            char_freq[c]=char_freq.get(c,0)-1
            if char_freq[c]<0:
                return False


        return True

        