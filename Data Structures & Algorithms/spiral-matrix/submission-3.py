class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0 , len(matrix)-1
        left ,right = 0, len(matrix[0]) -1
        res = []

        while top<=bottom and left<= right:
            for col in range(left,right+1):
                res.append(matrix[top][col])
            top+=1

            for row in range(top,bottom+1):
                res.append(matrix[row][right])
            right -=1

            if top<=bottom:
                for cols in range(right,left-1,-1):
                    res.append(matrix[bottom][cols])
                bottom-=1
            if left<=right:
                for rows in range(bottom,top-1,-1):
                    res.append(matrix[rows][left])
                left+=1
        return res