from functools import lru_cache
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        @lru_cache(maxsize = None)
        def path(i,j):
            if i==rows or j == cols:
                return 0
            if obstacleGrid[i][j] == 1:
                return 0
            if i==rows-1 and j==cols-1:
                return 1
            
            return path(i+1,j)+path(i,j+1)
        
        res = path(0,0)
        path.cache_clear()
        return res
