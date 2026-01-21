class Trie:

    def __init__(self):
        self.children={}
        self.isendofword=False
        

    def insert(self, word: str) -> None:
        current=self
        for letter in word:
            if letter not in current.children:
                current.children[letter]=Trie()
            current=current.children[letter]
        current.isendofword=True
        

    def search(self, word: str) -> bool:
        current=self
        for letter in word:
            if letter not in current.children:
                return False
            current=current.children[letter]
        return current.isendofword
        

    def startsWith(self, prefix: str) -> bool:
        current=self
        for letter in prefix:
            if letter not in current.children:
                return False
            current=current.children[letter]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)