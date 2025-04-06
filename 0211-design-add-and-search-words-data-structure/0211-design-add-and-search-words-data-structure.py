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