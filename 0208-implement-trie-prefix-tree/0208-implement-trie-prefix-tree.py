class Trie:

    def __init__(self):
        self.children={}
        self.is_end_of_word=False
        

    def insert(self, word: str) -> None:
        current = self
        for letter in word:
            if letter not in current.children:
                current.children[letter]=Trie()
            current=current.children[letter]
        current.is_end_of_word=True

    def search(self, word: str) -> bool:
        current=self 
        for letter in word:
            if letter not in current.children:
                return False 
            else: 
                current=current.children[letter]
        return current.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        current=self 
        for letter in prefix:
            if letter not in current.children:
                return False 
            else: 
                current=current.children[letter]
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)



# children is the name of the dictionary.

# Moving the Pointer with current = current.children[letter]
# This line is what allows you to navigate down the Trie as you insert characters. Here's what happens:

# current.children[letter] - This accesses the child node at key letter in the current node's children dictionary
# current =  - This updates your position variable to point to that child node

# Without this line, you'd stay at the root node for every character, creating all children directly under the root instead of building a proper tree path.
# Yes, self is the Root
# In the context of a Trie's methods:

# self refers to the Trie instance itself
# When you initialize current = self, you're starting at the root of the Trie
# The root node is simply the main Trie object that contains all other nodes

# \U0001f511 5. What are the keys and values in children?
# self.children = {}
# This dictionary maps:
# Key = a letter (string of length 1)
# Value = another Trie node


# i can understand current=current.next. the current will now point to whatever the next attribute of the current linked node is pointing to? but here children[letter] is a trie. not a linked noe?
# In a linked list, you do:
# current = current.next
# ➡️ And next is a pointer to the next node.
# ✅ You understand that perfectly.

# In a Trie:
# We don’t use .next, because each node could have many possible next nodes, not just one.
# So instead, we use a dictionary:
# current.children
# is a dictionary (also called a hash map). It maps from character → Trie node.
# So
# current.children['a'] = Trie()
# So when you write:
# current = current.children[letter]
# You’re doing the exact same thing as current = current.next, except:

# Instead of one next, you have many options ('a', 'b', 'z', etc.)

# You pick the one matching the current character
# So
# current.children[letter]
# ➡️ Means: “Get the next Trie node for this letter”
