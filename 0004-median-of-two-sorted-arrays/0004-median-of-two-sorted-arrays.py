class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1


        m=len(nums1)
        n=len(nums2)

        lo=0
        hi=m 

        half=(m+n+1)//2 

        while lo<=hi:
            i=(lo+hi)//2
            j=half-i 


            left1=nums1[i-1] if i>0 else float('-inf')
            right1=nums1[i] if i<m  else float('inf')
            left2=nums2[j-1] if j>0  else float('-inf')
            right2=nums2[j]  if j<n  else float('inf')

            if left1>right2:
                hi=i-1 
            elif left2>right1:
                lo=i+1
            else:
                max_left=max(left1,left2)
                min_right=min(right1,right2)
                if (m+n)%2==1:
                    return max_left
                return (max_left+min_right)/2 
                
        