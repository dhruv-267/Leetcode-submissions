from functools import lru_cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @lru_cache(maxsize=None)
        def path(i,j):
            if i == m or j==n:
                return 0
            if i==m-1 and j==n-1:
                return 1
            return path(i+1,j)+path(i,j+1)
        
        res = path(0,0)
        path.cache_clear()
        return res
        