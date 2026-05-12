class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc]==color:
            return image
        precol = image[sr][sc]
        rows = len(image)
        cols = len(image[0])
        q = collections.deque()
        q.append((sr,sc))
        direction = [[1,0],[0,1],[-1,0],[0,-1]]

        while q:
            for i in range(len(q)):
                r ,c = q.popleft()
                image[r][c]=color
    
                for dr ,dc in direction:
                    nr,nc = dr+r, dc+c
                    if 0<=nr<rows and 0<=nc<cols and image[nr][nc]==precol:
                        q.append((nr,nc))
                        
        return image
                        


