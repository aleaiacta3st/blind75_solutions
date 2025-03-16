class Solution:
    def maxArea(self, height: List[int]) -> int:
        #2 pointer approach
        #the pointers start at the xtremes and move inwards
        # key insight: only the lowest height must be moved inside
        # remember the shorter height decides the area
        # even if the greater height moved inwards to even greater height, 
        # the area would decrease as the width has decreased and the 
        # shorter height hasnt changed
        s1=0
        n=len(height)
        s2=n-1
        maxarea=(s2-s1)*min(height[s1],height[s2])
        #the above is the widest possible container. all the other combos we 
        # check will have a smaller width. if width is decreasing, the 
        # decrease in area can only be compensated by an increase in the 
        # shorter height.
        while (s1<s2):
            #<= in the line below is crucial. without it, we would descend into 
            #the maxarea calculation and if s1<s2, we will stuck in a loop
            #The mathematical truth is that when we have two equal constraints, 
            # breaking either one gives us the same opportunity to improve. The 
            # limitation could be broken from either end, with equal potential 
            # for victory.
            #As Frederick the Great once said: "He who defends everything defends 
            # nothing." In this algorithm, we must abandon one position to 
            # potentially find a greater one.
            if (height[s1]<=height[s2]):
                s1=s1+1
            elif(height[s1]>height[s2]):
                s2=s2-1 
            maxarea = max(maxarea,(s2-s1)*min(height[s1],height[s2]))
        return maxarea
                