class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        visited.add((0,0))
        minheap = [[grid[0][0],0,0]]
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        while minheap:
            t,r,c = heapq.heappop(minheap)
            if (r,c) == (n-1,n-1):
                return t
            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                if nr < 0  or nc <0 or nr == n or nc == n or (nr,nc) in visited:
                    continue 
                visited.add((nr,nc))
                heapq.heappush(minheap,[max(t,grid[nr][nc]),nr,nc])
            