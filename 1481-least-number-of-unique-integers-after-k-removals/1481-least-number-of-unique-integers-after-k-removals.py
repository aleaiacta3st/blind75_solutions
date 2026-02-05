class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        freq={}


        for num in arr:
            freq[num] = freq.get(num,0)+1 



        sorted_freq = sorted(freq.values())

        removed =0

        for f in sorted_freq:
            if k>=f:
                k=k-f
                removed=removed+1 
            else:
                break 


        return len(freq)-removed




        


        