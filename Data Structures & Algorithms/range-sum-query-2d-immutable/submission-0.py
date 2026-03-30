class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS = len(matrix)
        COLS = len(matrix[0])
        self.prefixSumMatrix = [[0] * (COLS+1) for _ in range(ROWS+1)]
        for i in range(ROWS):
            for j in range(COLS):
                self.prefixSumMatrix[i+1][j+1]= (matrix[i][j] + self.prefixSumMatrix[i+1][j] + self.prefixSumMatrix[i][j+1] - self.prefixSumMatrix[i][j])
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 = row1+1
        col1 = col1+1
        row2= row2+1
        col2 = col2+1
        
        return (self.prefixSumMatrix[row2][col2]+self.prefixSumMatrix[row1-1][col1-1]-self.prefixSumMatrix[row1-1][col2]-self.prefixSumMatrix[row2][col1-1])
