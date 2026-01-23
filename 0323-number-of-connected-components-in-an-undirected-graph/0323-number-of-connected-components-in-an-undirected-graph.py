class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))  # [0, 1, 2, ..., n-1]
    
        def find_leader(x):
            if parent[x] != x:
                return find_leader(parent[x])
            return x
        
        def union(a, b):
            leader_a = find_leader(a)
            leader_b = find_leader(b)
            if leader_a != leader_b:
                parent[leader_b] = leader_a
                return True   # merged two groups
            return False      # already same group
        
        components = n
        for a, b in edges:
            if union(a, b):
                components -= 1
        
        return components
        