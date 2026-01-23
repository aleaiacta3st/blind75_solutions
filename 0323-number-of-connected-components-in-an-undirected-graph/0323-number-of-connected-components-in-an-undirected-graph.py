class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))

        def find_leader(x):
            if parent[x]==x:
                return x 
            else:
                return find_leader(parent[x])


        def union(a,b):
            a_leader=find_leader(a)
            b_leader=find_leader(b)

            if a_leader!=b_leader:
                parent[b_leader]=a_leader
                return True

            return False

        components=n

        for a,b in edges:
            if union(a,b):
                components=components-1

        return components

        