class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n=len(heights)

        stack=[]

        max_area=0

        for i in range(n):
            while stack and heights[i]<heights[stack[-1]]:
                height=heights[stack.pop()]
                if not stack:
                    width=i
                else:
                    width=i-stack[-1]-1
                max_area=max(max_area,height*width)
            stack.append(i) 

        while stack:
            height=heights[stack.pop()]
            if not stack:
                width=n
            else:
                width=n-stack[-1]-1
            max_area=max(max_area,height*width)


        return max_area



            
        