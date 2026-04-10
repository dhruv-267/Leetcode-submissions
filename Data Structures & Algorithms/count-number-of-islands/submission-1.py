class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid),len(grid[0])
        

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            grid[r][c] = "0"
            while q:
                for i in range(len(q)):
                    cur_r,cur_c = q.popleft()

                    neighbours = [[1,0],[-1,0],[0,1],[0,-1]]
                    for dr, dc in neighbours:
                        nr, nc = cur_r+dr, cur_c+dc
                        if nr<0 or nc<0 or nr==rows or nc== cols or grid[nr][nc]=="0":
                            continue
                        grid[nr][nc] = "0"
                        q.append((nr,nc))
                    
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    bfs(i,j)
                    islands+=1
        
        return islands
            




        