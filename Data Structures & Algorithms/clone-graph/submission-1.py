"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        oldTonew = {}

        def dfs(node):
            if node in oldTonew:
                return oldTonew[node]
            copy = Node(node.val)
            oldTonew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        if not node:
            return None
        else:
            return dfs(node)
        