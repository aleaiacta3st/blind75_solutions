class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n=len(heights),len(heights[0])
        can_reach_atlantic=set()
        can_reach_pacific=set()
        
        def dfs_atlantic(i,j):
            if (i,j) not in can_reach_atlantic:
                can_reach_atlantic.add((i,j))
                for a,b in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    if 0<=a<m and 0<=b<n and heights[a][b]>=heights[i][j]:
                        dfs_atlantic(a,b)
        
        def dfs_pacific(i,j):
            if (i,j) not in can_reach_pacific:
                can_reach_pacific.add((i,j))
                for a,b in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    if 0<=a<m and 0<=b<n and heights[a][b]>=heights[i][j]:
                        dfs_pacific(a,b)

        for j in range(n):
            dfs_atlantic(m-1,j)

        for i in range(m):
            dfs_atlantic(i,n-1)

        for i in range(m):
            dfs_pacific(i,0)

        for j in range(n):
            dfs_pacific(0,j)

        intersection_set = can_reach_pacific & can_reach_atlantic

        final_list=[]

        for i in intersection_set:
            final_list.append(list(i))

        return final_list
        