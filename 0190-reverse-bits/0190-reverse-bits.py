class Solution:
    def reverseBits(self, n: int) -> int:
        number=0
        for i in range(32):#because 3 in 32 bit will be 
                        #preceded by many zeros
            number = number<<1 #shift the number to make place 
                            #for the last bit that will be 
                            # extracted in the next step
            if (n&1==1):#last bit is 1
                number = number+1 #number|1 will give the same result
                #if last bit is 0, number =number+0, no change in number
                #so there is no need of a separate else condition for it
            n=n>>1#push out the last bit,
                #we have already taken care of it
        return number
        