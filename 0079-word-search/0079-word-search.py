class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        visited=set()

        def dfs(x,y,index):
            if board[x][y] != word[index]:
                return False
            visited.add((x,y))
            index+=1
            if index == len(word):
                return True
            directions = [(-1, 0),  # up (x-1, y)
                            (1, 0),   # down (x+1, y)
                            (0, -1),  # left (x, y-1)
                            (0, 1)    # right (x, y+1)
                            ]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    if dfs(nx, ny, index):
                        return True
            visited.remove((x, y))
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    if dfs(i,j,0):
                        return True               
        return False
        