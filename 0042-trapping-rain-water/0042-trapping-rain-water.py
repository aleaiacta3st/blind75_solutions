class Solution:
    def trap(self, height: List[int]) -> int:

        n= len(height)

        stack=[]

        water=0

        for i,h in enumerate(height):
            while stack and height[stack[-1]]<h:
                base= stack.pop()
                if not stack:
                    break
                left=stack[-1]
                width = i -left -1
                bounded_height = min(height[left],height[i]) - height[base]

                water = water + (width*bounded_height)

            stack.append(i)


        return water
        