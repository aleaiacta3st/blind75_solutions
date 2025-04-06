class WordDictionary:

    def __init__(self):
        self.children={}
        self.is_end_of_word=False

        

    def addWord(self, word: str) -> None:
        current = self
        for letter in word:
            if letter not in current.children:
                current.children[letter]=WordDictionary()
            current=current.children[letter]
        current.is_end_of_word=True

        

    def search(self, word: str) -> bool:
        n = len(word)
        def wildcard(current, i):
            if i == n:
                return current.is_end_of_word
            if word[i] == '.':
                for letter in current.children:
                    if wildcard(current.children[letter], i + 1):
                        return True
                return False
            else:
                if word[i] not in current.children:
                    return False
                return wildcard(current.children[word[i]], i + 1)
        
        return wildcard(self, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)



# Your confusion: Why does recursion handle both '.' and non-'.' characters when I thought it was just for '.'?

# My answer: Unified recursion simplifies the code by managing both cases in one function, avoiding messy switches between iteration and recursion.


# The search method checks if a word (which may include wildcards like '.') exists in the trie.

# Arguments
# word: The string to search (e.g., "cat" or "c.t").
# current: The current node in the trie (starts at the root).
# i: The index in the word being processed (starts at 0).
# Algorithm & Logic
# Base Case:
# When i == len(word), the entire word has been processed.
# Return current.is_end_of_word (True if this node marks a complete word, False otherwise).
# Why? This ensures the search only succeeds if the word matches fully and ends at a valid word.
# Wildcard ('.'):
# If word[i] is '.', it matches any letter.
# Recursively search all child nodes of current for the rest of the word (increment i).
# Why? A wildcard means any character at this position is valid.
# Specific Letter:
# If word[i] is a letter (e.g., 'a'), recurse only on the child node for that letter (if it exists).
# Move to the next index (i + 1).
# Why? A letter must match exactly to continue the search.
# Why the Base Condition Matters
# The base condition (i == len(word)) ensures:

# The full word has been matched (no partial matches).
# The search ends at a node flagged as a complete word (is_end_of_word).
# Example
# Word = "cat": Follows 'c' → 'a' → 't', checks if 't' node is a word.
# Word = "c.t": At '.', tries all children of 'c', then matches 't'.