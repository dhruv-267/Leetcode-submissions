class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        visited = set()
        n = len(word)

        def dfs(i,r,c):
            if i == n:
                return True
            if (r,c) in visited or r<0 or c<0 or r>row-1 or c > col-1 or board[r][c] != word[i]:
                return False
            
            visited.add((r,c))
            res = dfs(i+1,r+1,c) or dfs(i+1,r,c+1) or dfs(i+1,r-1,c) or dfs(i+1,r,c-1)
            visited.remove((r,c))

            return res

        for r in range(row):
            for c in range(col):
                if dfs(0,r,c):
                    return True
        return False 
        