class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        row , col = len(heights), len(heights[0])

        def dfs(r,c,grp,prevht):
            if r < 0 or c < 0 or r == row or c == col or (r,c) in grp or heights[r][c] < prevht:
                return
            grp.add((r,c))
            dfs(r+1,c,grp,heights[r][c])
            dfs(r-1,c,grp,heights[r][c])
            dfs(r,c+1,grp,heights[r][c])
            dfs(r,c-1,grp,heights[r][c])
        
        for r in range(row):
            dfs(r,0,pac,0)
            dfs(r,col-1,atl,0)
        
        for c in range(col):
            dfs(0,c,pac,0)
            dfs(row-1,c,atl,0)
        res = []
        for a,b in pac & atl:
            res.append([a,b])
        return res


        