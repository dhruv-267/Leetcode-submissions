class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = {i:[] for i in range(n+1)}
        def dfs(node,par):
            if node in visited:
                return False
            visited.add(node)
            for nei in adj[node]:
                if nei!=par and not dfs(nei,node):
                    return False
            return True 

        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            visited = set()
            if not dfs(n1,-1):
                return [n1,n2]
        return []

        


            
  
        