class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        left=0
        right=n-1
        areamax=(right-left)*min(height[right],height[left])

        while left<right:
            if height[left]<=height[right]:
                left=left+1
            else:
                right=right-1
            area=(right-left)*min(height[left],height[right])
            areamax=max(areamax,area)

        return areamax
            
        