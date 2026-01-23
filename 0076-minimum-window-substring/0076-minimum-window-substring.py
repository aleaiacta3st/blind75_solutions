class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        n=len(s)
        left=0
        res_len=float('inf')
        res=[-1,-1]
        need_freq={}
        
        
        for c in t:
            need_freq[c]=need_freq.get(c,0)+1

        boxes=len(need_freq)
        ticked=0

        window_freq={}

        for right in range(n):
            window_freq[s[right]] = window_freq.get(s[right],0)+1

            if s[right] in need_freq and window_freq[s[right]]==need_freq[s[right]]:
                ticked=ticked+1

            while ticked==boxes:
                if right-left+1<res_len:
                    res_len=right-left+1
                    res=[left,right]
                
                window_freq[s[left]]-=1

                if s[left] in need_freq and window_freq[s[left]]<need_freq[s[left]]:
                    ticked=ticked-1

                left=left+1


        return s[res[0]:res[1]+1] if res_len!=float('inf') else ""


        