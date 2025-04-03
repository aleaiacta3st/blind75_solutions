class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s=="":
            return True 
        n=len(s)
        s=s.lower()
        only_alphanumeric=""
        for i in s:
            if i in ['0','1','2','3','4','5','6','7','8','9']:
                only_alphanumeric+=i
            if i in string.ascii_lowercase:
                only_alphanumeric+=i
        original=[] #this is a stack
        for i in only_alphanumeric:
            original.append(i)
        popped_out = ''
        for i in range(len(only_alphanumeric)):
            popped_out +=original.pop() 
        return only_alphanumeric==popped_out

# s = "hello"
# k = s       # k and s both point to "hello"
# s = s.upper()  # now s points to "HELLO", k still points to "hello"

# convert to lower case 
# remove any non alphanumeric chars 
# stack 
# pop 
# if both are equal. it is a palindrome.
        