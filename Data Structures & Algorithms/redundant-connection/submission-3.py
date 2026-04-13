class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]: # O(E*(V+E))
        n = len(edges)
        adj = {i:[] for i in range(n+1)}  # n+1 because vertices are numbered 1 to n instead of 0 to n-1!
        def dfs(node,par): #(V+E)
            if node in visited: 
                return False
            visited.add(node) #(V)
            for nei in adj[node]: #(E)
                if nei!=par and not dfs(nei,node):
                    return False
            return True 

        for n1,n2 in edges:    #O(E)
            adj[n1].append(n2)
            adj[n2].append(n1)
            visited = set()
            if not dfs(n1,-1):  #(E+V)
                return [n1,n2]
        return []

        


            
  
        