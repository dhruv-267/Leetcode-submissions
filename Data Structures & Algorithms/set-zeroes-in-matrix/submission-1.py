class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows , cols = len(matrix), len(matrix[0])
        row = set()
        col = set()
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        
        for i in range(rows):
            for j in range(cols):
                if i in row or j in col:
                    matrix[i][j] = 0

        
        