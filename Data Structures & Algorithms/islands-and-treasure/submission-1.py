class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid),len(grid[0])
        q = collections.deque()
        dist = 1
        direction = [[1,0],[-1,0],[0,1],[0,-1]]

        for r in range(row):
            for c in range(col):
                if grid[r][c]==0:
                    q.append([r,c])
        
        while q:
            for i in range(len(q)):
                r,c = q.popleft()

                for dr,dc in direction:
                    nr,nc = r + dr, c + dc
                    
                    if nc<0 or nr < 0 or nc == col or nr == row or grid[nr][nc]!=2147483647:
                        continue
                    q.append([nr,nc])
                    grid[nr][nc] = dist
            
            dist+=1
        

        