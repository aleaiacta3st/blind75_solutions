class TrieNode:
    def __init__(self):
        self.children={}
        self.isendofword=False



class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        

    def addWord(self, word: str) -> None:
        curr=self.root

        for letter in word:
            if letter not in curr.children:
                curr.children[letter]=TrieNode()
            curr=curr.children[letter]
        curr.isendofword = True
        

    def search(self, word: str) -> bool:
        def dfs(idx,node):
            if idx==len(word):
                return node.isendofword
            c=word[idx]

            if c=='.':
                for child in node.children.values():
                    if dfs(idx+1,child):
                        return True
                return False 
            else:
                if c not in node.children:
                    return False
                else:
                    return dfs(idx+1,node.children[c])
        
        return dfs(0,self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)