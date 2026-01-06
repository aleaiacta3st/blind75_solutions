class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
    
        need_freq = {}
        for c in t:
            need_freq[c] = need_freq.get(c, 0) + 1
        
        window_freq = {}
        
        freqs_met, freqs_needed = 0, len(need_freq)
        left = 0
        res, res_len = [-1, -1], float('inf')
        
        for right in range(len(s)):
            right_char = s[right]
            window_freq[right_char] = window_freq.get(right_char, 0) + 1
            
            if right_char in need_freq and window_freq[right_char] == need_freq[right_char]:
                freqs_met += 1
            
            while freqs_met == freqs_needed:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                
                window_freq[s[left]] -= 1
                if s[left] in need_freq and window_freq[s[left]] < need_freq[s[left]]:
                    freqs_met -= 1
                left += 1
        
        return s[res[0]:res[1]+1] if res_len != float('inf') else ""
        

# distinct_required_characters = len(t_scan)
# This is a very crucial idea 
# we must make a frequency counter of t 
# then in the main for-loop 
# if we come across a character in t that is in s 
# we reduce its frequency by 1 
# we have found all our targets in s when frequency of all elements 
# in t_scan becomes zero 
# when we find frequency of a number has gone to 0, we reduce the number of 
# distinct characters needed by 1 
# when number of distinct characters needed becomes 0, it means we have all 
# our targets in our current window 
# store its start pos and window size 

# now we try to see if this solution can be improved 
# we try if we can find an even shorter window by bringing left forward
# when bringing it forward 2 cases arise
# we lose a target character 
# we don't lose a target char - we dont need to do anything,just continue
# when we lose a target char 
#  we need to increase its frequency by 1 and 
# increase the distinct char found by 1 only if the freq of this char 
# is increasing from 0 to 1 


# for every i, we check a range of valid lefts by bringing left forward. correct?
# lets suppose teh valid window breaks at a left
# now there are some probable lefts between the point where the window broke and i 
# what about these lefts? the window break at a left? but maybe there will be a 
# valid window just after that point?
# if such a left exists then we dont consider that left with current i again.
# how do we explain this seeming anomoly?

# When moving left forward causes our window to become invalid 
# (by losing a required character), any further positions between that left 
# and i cannot form valid windows with the current i.

# Think about it: If removing a character at position left-1 broke our window, 
# then any window starting after that position would still be missing that 
# critical character. We can prove mathematically that no valid window exists 
# in this range.

# That's why we exit the contraction loop and continue with expanding our '
# 'right pointer. It's not that we're ignoring potential solutions - we've 
# proven they cannot exist!

# This optimization is what gives sliding window algorithms their efficiency. 
# Like a chess grandmaster who doesn't waste time analyzing proven losing positions,'
# ' our algorithm intelligently prunes unpromising paths.
# The beauty of this approach is that we never miss an optimal solution while 
# avoiding unnecessary checks.

# You don’t need to revisit skipped lefts because you already proved that they 
# can’t be the start of a smaller valid window with the current i.


            
# when i have a valid window, why do i move my left regardless of the element 
# i am leaving out of my window is a char of t

# You want to test at every left. the previous i which formed a valid window 
# is already stored if it is the minimum seen so far. 

# The loop also makes sure that i takes every available value to see if a better 
# solution can be formed.

# When you have a valid window, you want to test every possible contraction to 
# find the minimum valid window. That's why you need to move left regardless of '
# 'what character you're removing.
# The genius of the sliding window pattern is in this methodical 
# expansion-contraction cycle:

# Expand the right side until you have a valid window
# Contract from the left as much as possible until you'd break the valid window
# Record the smallest valid window found during contraction
# Continue expanding from the right to find new valid windows

# Even if the left character is part of your target, you still need to try 
# removing it. If doing so breaks your valid window (because you no longer have 
# enough of that character), your distinct_required_characters counter 
# will increase above 0, and you'll exit the contraction loop.


# return s[start_pos:i+1]
# is this also right
# No, return s[start_pos:i+1] would not be correct. Here's why:
# By the time your loop finishes, i will have traversed through the 
# entire string to its end position. Your minimum window might have been 
# found much earlier in the string. Using i+1 as the end point would 
# return a substring that starts at your minimum window's beginning but '
# 'extends all the way to the end of the string.
# start position is upadted only when the current window length is smaller 
# than the smallest window seen so far. It's our way of "bookmarking" where 
# the best solution we've found so far begins.





# A critical part of the sliding window technique is that once you find a valid 
# window, you need to try to make it smaller by moving the left pointer forward 
# until the window becomes invalid, then continue expanding with the right pointer
#  again.