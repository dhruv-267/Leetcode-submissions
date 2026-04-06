class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pDiag = set()
        nDiag = set()
        board = [["."]*n for row in range(n)]
        res = []

        def dfs(i):
            if i == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or i+c in pDiag or i-c in nDiag:
                    continue
                
                col.add(c)
                pDiag.add(i+c)
                nDiag.add(i-c)
                board[i][c] = "Q"
                dfs(i+1)
                col.remove(c)
                pDiag.remove(i+c)
                nDiag.remove(i-c)
                board[i][c] = "."
        
        dfs(0)
        return res


