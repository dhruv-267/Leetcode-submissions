from functools import lru_cache
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        lastrow = [0]*(cols+1)
        for row in range(rows-1,-1,-1):
            currow = [0]*(cols+1)

            for col in range(cols-1,-1,-1):
                if obstacleGrid[row][col]==1:
                    currow[col]=0
                    continue
                if row == rows-1 and col == cols-1:
                    currow[col]=1
                    continue
                currow[col] = lastrow[col]+currow[col+1]
            lastrow = currow

        return lastrow[0]