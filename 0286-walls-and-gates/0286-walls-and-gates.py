class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        treasures=set()

        m=len(rooms)
        n=len(rooms[0])

        for r in range(m):
                for c in range(n):
                    if rooms[r][c]==0:
                        treasures.add((r,c))

        def bfs(treasures):
            queue=deque(treasures)
            visited=set(treasures)
            while queue:
                r,c=queue.popleft()
                for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nr,nc=r+dr,c+dc
                    if 0<=nr<m and 0<=nc<n and (nr,nc) not in visited and rooms[nr][nc] == 2147483647:
                        rooms[nr][nc]=rooms[r][c]+1
                        visited.add((nr,nc))
                        queue.append((nr,nc))




        bfs(treasures)