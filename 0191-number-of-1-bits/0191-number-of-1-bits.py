class Solution:
    def hammingWeight(self, n: int) -> int:
        count1=0
        while (n!=0):
            #if condition checks if the last bit 
            # of the number is 1
            if (n&1==1):
                count1=count1+1
            #right shift by 1 eliminates the 
            # last bit that we have already checked
            n=n>>1
        return count1
        