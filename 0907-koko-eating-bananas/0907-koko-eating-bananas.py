class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n=len(piles)
        lo=1
        hi=max(piles)
        ans=hi
        while lo<=hi:
            hours=0
            mid=(hi+lo)//2
            for i in range(n):
                hours+=math.ceil(piles[i]/mid)
            if hours<=h:
                ans=mid
                hi=mid-1 
            else:
                lo=mid+1
        return ans
        