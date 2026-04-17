import sys
from functools import lru_cache

sys.setrecursionlimit(20000)

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        direction = [[0,1],[0,-1],[1,0],[-1,0]]

        @lru_cache(maxsize=None)
        def dfs(i,j):
            maxlen = 0
            for dr,dc in direction:
                nr,nc= dr+i,dc+j
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[i][j]:
                    maxlen = max(maxlen, dfs(nr, nc))
            return 1+maxlen
        
        maxres = 0
        for i in range(rows):
            for j in range(cols):
                maxres = max(maxres,dfs(i,j))
        dfs.cache_clear()
        return maxres
