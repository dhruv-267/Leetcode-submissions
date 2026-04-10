class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid),len(grid[0])
        q = collections.deque()
        time, fresh = 0 , 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append([r,c])

        while q and fresh>0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr , nc = r+dr, c+dc
                    if nr<0 or nc<0 or nr == row or nc == col or grid[nr][nc]!=1:
                        continue
                    grid[nr][nc] = 2
                    fresh-=1
                    q.append([nr,nc])
            time+=1
        return time if not fresh else -1
        

                    
                
        