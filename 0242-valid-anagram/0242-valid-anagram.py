class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n=len(s)
        m=len(t)
        if n!=m:
            return False
        t_scan = {}
        for i in range(m):
            if t[i] not in t_scan:
                t_scan[t[i]]=1
            else:
                t_scan[t[i]]+=1
        distinct_chars = len(t_scan)
        left=0
        for i in range(n):
            if s[i] in t_scan:
                t_scan[s[i]]-=1
                if t_scan[s[i]]==0:
                    distinct_chars-=1
        return (distinct_chars==0)
        