class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams={}
        n=len(strs)
        for i in range(n):
            if ''.join(sorted(strs[i])) in grouped_anagrams:
                grouped_anagrams[''.join(sorted(strs[i]))].append(strs[i])
            else:
                grouped_anagrams[''.join(sorted(strs[i]))] = [strs[i]]
        return list(grouped_anagrams.values())

# sorted(strs[i]):
# Takes a string (like "eat") and converts it to a sorted list of characters
# Example: "eat" → ['a', 'e', 't']
# This gives us our characters in alphabetical order

# ''.join(...):
# The empty string '' is the "glue" between elements
# The join() method combines all characters in the list into a single string
# Example: ['a', 'e', 't'] → "aet"

# Strings in Python are immutable, which means once created, they 
# cannot be changed.

# How list(grouped_anagrams.values()) Works
# This line transforms your dictionary of anagram groups into the final output format. Let me break it down:

# grouped_anagrams.values()

# Returns a special "view object" containing all values from your dictionary
# In our case, these values are lists of strings (groups of anagrams)


# list(...)

# Converts this view object into a regular Python list
# Creates a list of lists, where each inner list is one anagram group

# grouped_anagrams = {
#     "aet": ["eat", "tea", "ate"],
#     "ant": ["tan", "nat"]
# }

# # grouped_anagrams.values() gives: dict_values([["eat", "tea", "ate"], 
# # ["tan", "nat"]])
# # list(...) converts to: [["eat", "tea", "ate"], ["tan", "nat"]]
        