class Solution:
    class Trie:
        def __init__(self):
            self.children={}
            self.is_end_of_word=False
            self.word=None

        def insert(self, word: str) -> None:
            current = self
            for letter in word:
                if letter not in current.children:
                    current.children[letter] = Solution.Trie()  # Use Solution.Trie instead of Trie
                current = current.children[letter]
            current.is_end_of_word = True 
            current.word = word

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        final = set()  # You defined this as a set
        visited = set()

        word_trie = Solution.Trie()  # Use Solution.Trie instead of Trie
        for word in words:
            word_trie.insert(word)

        def backtrack(x, y, current):
            if board[x][y] not in current.children:
                return False 
            current = current.children[board[x][y]]
            if current.is_end_of_word:
                final.add(current.word)  # Use add for sets, not append
                current.is_end_of_word = False
            visited.add((x, y))
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in directions:
                nx = x + dx 
                ny = y + dy 
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    backtrack(nx, ny, current)
            visited.remove((x, y))
            return False
        
        for i in range(m):
            for j in range(n):
                backtrack(i, j, word_trie)  # Pass word_trie, not current
                
        return list(final)  # Convert set to list before returning


        