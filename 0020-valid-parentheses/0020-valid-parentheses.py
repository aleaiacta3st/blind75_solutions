class Solution:
    def isValid(self, s: str) -> bool:
        if s is None:
            return True
        parentheses = {')': '(', ']': '[', '}': '{'}
        stacker=[]
        for i in s:
            if i in parentheses.values():
                stacker.append(i)
            if i in parentheses:
                if not stacker or parentheses[i] != stacker[-1]:
                    return False
                stacker.pop()
        return len(stacker)==0
        


# [({)} is not valid though each opener has its closer match. Opener is of one kind, closer is of a different kind. 
# A valid sequence will always be of the form [({})] - an opener in the middle will be immediately followed by its closer. 
# and when you po that pair out as in the code you will the same pattern again. An opener immediately followed by its matching closer.

# if opener - push into stack 
# if closer - if last opener is its match - pop the opener 
#           -if last opener not a match - invalid 

# stack grows only when it encounters an opener 
# so it becomes empty when each of the openers gets its match and popped out
# so, if stack is empty, it is a valid parentheses

# suppose there are more closers than there are openers, then stack gets emptied first
# we will be left with a lone closer which needs to fall into the second if statement 
# but that block involves accessing stacker[-1] which throws up an error if stack is empty 
# so add a check to see that the stack is not empty

# think about cases: 
# where there are more openers than closers
# where there are more closers than openers 

# when there are more closers than openers, the stack gets emptied first - return False immediately. just because the stack is empty, doesnt make it valid because we have an unmatched closer. 

# after eliminating such cases check length of stack. if 0 then valid 
# if not 0, openers have not found matching closers. Invalid.