class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequency={}

        for num in nums:
            frequency[num]=frequency.get(num,0)+1


        min_heap=[]

        for num,freq in frequency.items():
            heapq.heappush(min_heap,(freq,num))
            if len(min_heap)>k:
                heapq.heappop(min_heap)


        return [num for freq,num in min_heap]
        