class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_scan={}
        n=len(t)
        m=len(s)
        smallest_window = float('inf')
        start_pos=0
        for i in range(n):
            if t[i] not in t_scan:
                t_scan[t[i]]=1
            else:
                t_scan[t[i]]+=1 
        distinct_required_characters = len(t_scan)
        left=0

        for i in range(m):
            if s[i] in t_scan:
                t_scan[s[i]]-=1
                if (t_scan[s[i]])==0:
                    distinct_required_characters-=1
                if distinct_required_characters==0:
                    while distinct_required_characters==0:
                        current_window_len = i-left+1
                        if current_window_len < smallest_window:
                            smallest_window = current_window_len
                            start_pos = left
                        left=left+1
                        if s[left-1] not in t_scan:
                            continue
                        else:
                            if t_scan[s[left-1]] ==0:
                                t_scan[s[left-1]]+=1
                                distinct_required_characters+=1
                            else:
                                t_scan[s[left-1]]+=1
        if smallest_window==float('inf'):
            return ""
        else:
            return s[start_pos:start_pos + smallest_window]
        