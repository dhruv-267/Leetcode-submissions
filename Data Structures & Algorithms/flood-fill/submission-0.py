class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc]==color:
            return image
        precol = image[sr][sc]
        rows = len(image)
        cols = len(image[0])
        visited = set()
        q = collections.deque()
        q.append((sr,sc))
        visited.add((sr,sc))
        direction = [[1,0],[0,1],[-1,0],[0,-1]]

        while q:
            for i in range(len(q)):
                r ,c = q.popleft()
    
                image[r][c] = color
                visited.add((r,c)) 

                for dr ,dc in direction:
                    nr,nc = dr+r, dc+c
                    if nr<0 or nc<0 or nr==rows or nc == cols or (nr,nc) in visited or image[nr][nc]==color:
                        continue
                    if image[nr][nc]==precol:
                        q.append((nr,nc))
        return image
                        


