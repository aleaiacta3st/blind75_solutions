class Solution:
    def reorganizeString(self, s: str) -> str:

        n=len(s)

        result=[]

        frequency={} 

        for ch in s:
            frequency[ch]=frequency.get(ch,0) + 1

        if max(frequency.values())>((n+1)//2):
            return ""

        heap=[]

        for ch,freq in frequency.items():
            heapq.heappush(heap,(-freq,ch)) 

        prev_freq=0
        prev_char="" 

        while heap:
            neg_freq,ch=heapq.heappop(heap)
            freq=-neg_freq
            freq=freq-1
            result.append(ch)
            if prev_freq:
                heapq.heappush(heap,(-prev_freq,prev_char))
            prev_freq=freq
            prev_char=ch 

        
        return "".join(result)





        


        