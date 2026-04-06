class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW , COL = len(board), len(board[0])
        boardset = set()

        def backtrack(i, r, c):

            if i == len(word):
                return True
            
            if (r,c) in boardset or (c < 0 or r < 0) or (r > ROW-1 or c > COL-1) or board[r][c] != word[i]:
                return False

            boardset.add((r,c))
            res = backtrack(i+1,r+1,c) or backtrack(i+1,r-1,c) or backtrack(i+1,r,c+1) or backtrack(i+1,r,c-1) 
            boardset.remove((r,c))

            return res
        
        for r in range(ROW):
            for c in range(COL):
                if backtrack(0,r,c):
                    return True
        return False


        