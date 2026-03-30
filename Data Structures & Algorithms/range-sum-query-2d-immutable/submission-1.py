class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.row = len(matrix)
        self.col = len(matrix[0])
        self.sumMat = []

        for i in range(self.row +1):
            self.temp = []
            for j in range(self.col+1):
                self.temp.append(0)
            self.sumMat.append(self.temp)
        for i in range(1,self.row +1):
            for j in range(1,self.col+1):
                self.sumMat[i][j] = matrix[i-1][j-1]+self.sumMat[i-1][j]+self.sumMat[i][j-1]-self.sumMat[i-1][j-1]

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sumMat[row2+1][col2+1]-self.sumMat[row1][col2+1] - self.sumMat[row2+1][col1]+self.sumMat[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)