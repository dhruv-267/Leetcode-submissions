class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        col = {}
        semi = {}
        for r in range(9):
            for c in range(9):
                row[r]= row.get(r,[])
                col[c]= col.get(c,[])
                semi[(r//3,c//3)] = semi.get((r//3,c//3),[])
                if board[r][c] not in ["1","2","3","4",'5','6','7','8','9']:
                    continue
                elif board[r][c] in col[c] or board[r][c] in row[r] or board[r][c] in semi[(r//3,c//3)]:
                    return False
                else:
                    row[r].append(board[r][c])
                    col[c].append(board[r][c])
                    semi[(r//3,c//3)].append(board[r][c])
        print("Row : ",row,"\nCol : ",col)
        return True
