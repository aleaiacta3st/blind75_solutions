class TrieNode:
    def __init__(self):
        self.children={}
        self.isendofword=False

    def insert(self, word):
        curr=self
        for letter in word:
            if letter not in curr.children:
                curr.children[letter]=TrieNode()
            curr = curr.children[letter]
        curr.isendofword=True



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m=len(board)
        n=len(board[0])

        root=TrieNode()

        for w in words:
            root.insert(w)


        res=set()
        visited=set()

        def dfs(r,c,node,word):
            if r<0 or r>=m or c<0 or c>=n or (r,c) in visited or board[r][c] not in node.children:
                return

            visited.add((r,c))

            node=node.children[board[r][c]]

            word=word+board[r][c]

            if node.isendofword is True:
                res.add(word)

            dfs(r,c-1,node,word)
            dfs(r,c+1,node,word)
            dfs(r-1,c,node,word)
            dfs(r+1,c,node,word)

            visited.remove((r,c))




        for i in range(m):
            for j in range(n):
                if board[i][j] in root.children:
                    dfs(i,j,root,"")

        return list(res)






        