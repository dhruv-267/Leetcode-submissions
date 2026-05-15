class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # When a graph is valid tree?
        # A valid tree doesnt have cycle! Graph may have.
        # "A" valid tree mean there must be only 1 tree made from graph, not multiple disjoint trees.
        
        #graph is valid tree if no cycle detected.. visited == #nodes in graph 

        adj = { i:[] for i in range(n)}
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set()
        def dfs(node,par):
            if node in visited:
                return False
            visited.add(node)
            for neighbour in adj[node]:
                if neighbour!=par and not dfs(neighbour,node): return False
            return True

        return dfs(0,-1) and len(visited)==n