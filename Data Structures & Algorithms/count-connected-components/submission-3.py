
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [1] * n
        
        def find(n1): # Find parent of n1
            if n1 != parent[n1]:
                parent[n1] = find(parent[n1])  
            return parent[n1]
            
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
            elif rank[p1] < rank[p2]:
                parent[p1] = p2
            else:
                parent[p2] = p1
                rank[p1] += 1
                
            return True
        
        components = n
        for src, dst in edges:
            if union(src, dst):
                components -= 1

        return components