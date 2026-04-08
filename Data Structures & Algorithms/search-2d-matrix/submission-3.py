class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS , COLS = len(matrix), len(matrix[0])
        if target < matrix[0][0] or target > matrix[ROWS-1][COLS-1]:
            return False
        
        low, high = 0, ROWS-1
        while low <=high:
            mid = (low+high)//2
            
            if target < matrix[mid][0]:
                high = mid -1
            elif target > matrix[mid][-1]:
                low = mid + 1
            else:
                break
        row = mid
        low = 0 
        high = COLS-1

        while low <= high:
            mid = (low+high)//2
            if target < matrix[row][mid]:
                high = mid -1
            elif target > matrix[row][mid]:
                low = mid + 1
            else:
                return True
        return False
        
        