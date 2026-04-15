class Solution:
    def climbStairs(self, n: int) -> int:
        i , j  = 1 , 1   #n-1th place ans , nth place ans 
        for _ in range(n-1):
            temp = i
            i = i+j
            j = temp
        return i
