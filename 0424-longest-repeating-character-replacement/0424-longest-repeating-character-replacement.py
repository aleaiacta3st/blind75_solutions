class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency_tracker = {}
        left=0
        n=len(s)
        max_frequency=0
        longest=0
        for i in range(n):
            if s[i] not in frequency_tracker:
                frequency_tracker[s[i]]=1 
            else:
                frequency_tracker[s[i]]+=1
            max_frequency=max(max_frequency,frequency_tracker[s[i]])
            while (i-left+1)-max_frequency > k:
                frequency_tracker[s[left]]-=1
                left+=1
            longest=max(longest,i-left+1)
        return longest


# Summary of the Sliding Window Approach for Longest Repeating Character Replacement

# Valid Window Invariant
# At all times, the algorithm maintains this key condition:
# (window size) - (max frequency of a single character in the window) ≤ k
# This means the current window can be made uniform with at most k character 
# replacements.

# Why Keep the Window Valid?
# Instant Candidate: Every valid window is a potential answer, 
# so you don’t miss any possible solution.

# No Wasted Exploration: The moment it becomes invalid 
# (needs more than k replacements), you move the left pointer to discard part 
# of the window until you’re back within budget.

# Role of the Left Pointer
# Whenever you add a new character on the right and exceed the allowed 
# replacements, you shrink the window from the left until it’s valid again.

# This constant fix-up ensures each window you consider could still be the 
# longest valid substring.

# Efficiency

# The approach naturally does just one left-to-right pass (O(n)), 
# because you never linger in invalid territory.

# By maintaining the invariant at all times, you capture the maximum possible 
# valid window length on-the-fly.

# In essence, the discussion shows how sliding window methods can efficiently 
# track the largest contiguous segment satisfying a constraint, leveraging the idea that as soon as you break the constraint, you incrementally shrink from the left until the window is valid once more.



# When we talk about “removing characters that contributed to making the window 
# invalid,” it doesn’t literally mean that the character at the left pointer 
# caused the invalidity all by itself. Rather, the entire window needs too many 
# replacements. Because this is a sliding window over a contiguous substring, 
# the only systematic way to shrink the window is by advancing the left pointer.

# Why specifically the left pointer? Because:
# We’re dealing with a contiguous substring, so we can’t remove arbitrary 
# characters from the middle—only from an end.

# The sliding window method operates by expanding from the right and 
# contracting from the left. Whenever the cost (window size minus max frequency) 
# exceeds k, we shrink from the left until the window is valid again.

# By methodically moving the left pointer and adjusting frequencies, we 
# systematically explore all possible valid windows in a single pass (O(n)) 
# rather than trying random removals that would break contiguity or require 
# heavier computations.

# So, the character at the left pointer isn’t necessarily “to blame”—it’s just 
# the logical place to shrink so we can eventually land on every valid substring. 
# That’s how the sliding window approach maintains its simplicity and efficiency.



# max_frequency=max(max_frequency,frequency_tracker[s[i]])
# s[i] is the newest char added
# so its frequency increased and has a chance of being 
# greater than max frequency 
# so it is enough if we compare the max frequency with
# frequency s[i]
# This works because:
# When adding a character, only that character's frequency increases
# All other frequencies remain unchanged
# So the new maximum can only be either:
# The previous maximum (unchanged)
# The frequency of the newly added character (if it's now greater)

# In any window, we do not know which character has the most frequency 
# We just know the highest frequency in that window. it could be any char

# Why the Window Should Always Be Valid
# In “Longest Repeating Character Replacement,” you’re looking for the 
# longest substring where at most k replacements turn every character into 
# the same letter. A window is called valid if you could achieve that goal 
# within the current window using ≤ k replacements. Keeping the window 
# valid at every step means:

# Every Window Is a Potential Answer
# Because your window is always valid, its size is always a genuine candidate 
# for “longest valid substring.” If you ever find a bigger valid window, you can 
# update your best answer on the spot.

# You Don’t Waste Time
# There’s no sense in exploring windows that can’t ever be turned into a 
# uniform string with ≤ k replacements. By ensuring the window is valid, 
# you’re continually focused on possibilities that might improve your answer.

# What You’re Really Learning Here

# Invariant Maintenance: You’re seeing how to maintain the 
# condition “(window size) − (most frequent character’s count) ≤ k” at all times.
# This is the sliding window invariant that makes the algorithm correct and 
# efficient.

# One-Pass Efficiency: Because you always repair invalid windows right away, 
# you only scan from left to right once, leading to a time-efficient approach.

# Subproblem Insight: You’re getting a general framework for problems where 
# you want the longest (or shortest) subarray/substring that meets a certain 
# condition—sliding window often shines here.

# Essentially, the discussion reveals how a sliding window “expands” and 
# “contracts” to track the longest substring still meeting your constraints—in 
# this case, ≤ k replacements needed. It’s a way to ensure you never 
# miss a potential best solution, and you never waste time on clearly 
# impossible cases.

# Because your algorithm immediately shrinks the window whenever it 
# exceeds the allowed replacements (that is, whenever the window becomes invalid),
# you never continue exploring those invalid states. In other words, the 
# moment you detect “(window size − max frequency) > k,” you:

# Stop expanding in that exact state (so you don’t “explore” an impossible 
#                                     scenario further).

# Advance the left pointer to discard some part of the window until it 
# requires ≤ k replacements again (making it valid).

# This ensures your window is always brought back to a “potentially answer-worthy”
# state right away—so you never waste time doing extra work on clearly 
# unsalvageable windows. By maintaining that validity condition at all times, 
# you efficiently explore only those substrings that might actually become 
# the longest valid one.


# What Is an Invariant?
# An invariant is a rule or condition that your algorithm promises to keep true 
# at every moment. Imagine it as a “checkpoint” your sliding window must 
# always satisfy.
# (window_size) - (count_of_most_frequent_character_in_the_window) <= k
# “The total number of characters we must change in this window 
# (to make them all the same) is no more than k.”
# Whenever we add a new character to the window and violate this rule, 
# we shrink the left side until we’re back in compliance.

# Why It Matters
# Every Window Is a Valid Candidate
# If a window satisfies (window_length) - (max_freq) <= k, 
# then that substring could be turned into all one character using ≤ k 
# replacements. This means at any point, if you measure the window’s size, 
# it’s a legitimate contender for the answer.

# No Wasted Exploration
# The second the window can’t be made uniform with k replacements, 
# you stop and shrink it (no extra time spent in invalid states).

# One-Pass Efficiency
# You move from left to right exactly once, adjusting the left pointer 
# only as needed. This keeps the overall algorithm O(n).

# Hence, the “sliding window invariant” ensures you only track windows that 
# can possibly solve the problem. As soon as one doesn’t fit the constraint, 
# you fix it by advancing the left pointer—restoring the invariant and 
# continuing on.

# This means at any point, if you measure the window’s size, it’s a legitimate 
# contender for the answer.

# ok. i understand the above sentence. but how is this windows accounting 
# for all legitimate contenders? why cant there be legitimate contendors that 
# the windows cannot account for?

# Because the algorithm systematically expands and shrinks over every position 
# in the string (from left to right), it never “jumps over” a possible valid 
# window. Here’s the essence:

# We Expand as Far as We Can
# For each position of the right pointer, we keep pushing it to the right as 
# long as the window remains valid.
# If there’s a larger valid substring starting at or before the current left pointer, we’ll naturally discover it during this expansion phase.

# We Shrink Only When Invalid
# If we ever exceed the replacement limit (the window is invalid), we move the 
# left pointer up just enough to restore validity.
# This ensures we don’t waste time in invalid territory, but we also don’t 
# skip any contiguous stretch of the string that could be valid.

# One Continuous Sweep
# Because the right pointer scans from the beginning to the end of the string, 
# and the left pointer only moves forward (never backward), every possible 
# start/end configuration is checked (either explicitly or implicitly) in 
# the process.
# If a bigger valid window could exist at some point, the algorithm—by 
# always expanding to the maximum valid size—will find and record that longer 
# length.

# In other words, if there was a longer valid window, the algorithm would have 
# already expanded to include it, because it never stops expanding the 
# right boundary while the window is valid and never pulls the left boundary 
# in unless it must. That’s why all “legitimate contenders” for the maximum 
# valid substring length get accounted for.
        