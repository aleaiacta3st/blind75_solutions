class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n=len(isConnected)

        parent=list(range(n))

        def find_leader(x):
            if x==parent[x]:
                return x
            else:
                return find_leader(parent[x])



        def union(i,j):
            leader_i = find_leader(i)
            leader_j = find_leader(j)

            if leader_i!=leader_j:
                parent[leader_j]=leader_i
                return True
            else:
                return False



        provinces = n


        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1:
                    if union(i,j):
                        provinces=provinces-1


        return provinces


        

        

        