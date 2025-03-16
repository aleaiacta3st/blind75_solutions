class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        # ensure x >= y
        # this way if they ahve opposite signs, 
        # adding them won't land us in negative territory
        if x < y:
            return self.getSum(b, a)  
        #recursion happens only once
        sign = 1 if a > 0 else -1
        #we have ensured a to be the absolute biggest number. 
        # so sign depends on a and not on b.
        
        if a * b >= 0:#same sign, so just add the numbers. 
                    #sign will be added at the end.
            # sum of two positive integers
            while y:
                x, y = x ^ y, (x & y) << 1
        else: #we need to subtract
            # difference of two positive integers
            while y:
                x, y = x ^ y, ((~x) & y) << 1
        
        return x * sign
        