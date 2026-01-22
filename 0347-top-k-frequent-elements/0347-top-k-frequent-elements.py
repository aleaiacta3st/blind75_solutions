class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res=[]

        n=len(nums)

        frequency={}

        for num in nums:
            frequency[num]=frequency.get(num,0)+1


        buckets=[[] for _ in range(n+1)]

        for num,freq in frequency.items():
            buckets[freq].append(num)


        for freq in range(n,-1,-1):
            for num in buckets[freq]:
                res.append(num)
                if len(res)==k:
                    return res


    

        