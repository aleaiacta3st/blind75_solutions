class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        freq={}

        n=len(arr)

        for num in arr:
            freq[num] = freq.get(num,0)+1


        sorted_freqs =sorted(freq.values())

        removed =0


        for f in sorted_freqs:
            if k>=f:
                k=k-f
                removed=removed+1
            else:
                break 


        return len(freq)-removed


        


        


        