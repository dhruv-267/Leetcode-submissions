class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        visited = set() #(r,c)
        visited.add((0,0))
        minheap = [[grid[0][0],0,0]]    #(t,r,c)
        
        while minheap:
            w,r,c = heapq.heappop(minheap)
            if (r,c) == (n-1,n-1):
                return w
            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                if nr<0 or nc<0 or nr==n or nc==n or (nr,nc) in visited:
                    continue
                visited.add((nr,nc))
                heapq.heappush(minheap,[max(grid[nr][nc],w),nr,nc])
        return res
