class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = {}



        def dfs(i,j,prev):
            if i<0 or j<0 or i==rows or j==cols or matrix[i][j] <= prev:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            maxlen = 0
            maxlen = max(maxlen,1+dfs(i+1,j,matrix[i][j]))
            maxlen = max(maxlen,1+dfs(i-1,j,matrix[i][j]))
            maxlen = max(maxlen,1+dfs(i,j+1,matrix[i][j]))
            maxlen = max(maxlen,1+dfs(i,j-1,matrix[i][j]))
            dp[(i,j)] = maxlen
            return maxlen
        
        for i in range(rows):
            for j in range(cols):
                dfs(i,j,-1)
        return max(dp.values())
