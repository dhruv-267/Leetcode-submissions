class Solution:
    def climbStairs(self, n: int) -> int:
        i , j = 1,1

        for _ in range(n-1):
            temp = i
            i = i + j
            j = temp
        return i 