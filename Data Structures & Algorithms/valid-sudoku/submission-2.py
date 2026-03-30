class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashmap = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                row = f'{board[i][j]} in row{i}'
                col = f'{board[i][j]} in col{j}'
                sqr = f'{board[i][j]} in sqr{i//3}{j//3}'

                if (row in hashmap) or (col in hashmap) or (sqr in hashmap):
                    return False
                else:
                    hashmap[row] = 1
                    hashmap[col] = 1
                    hashmap[sqr] = 1
        return True 
        