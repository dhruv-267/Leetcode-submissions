class Solution:
    def climbStairs(self, n: int) -> int:
        sqrt5 = math.sqrt(5)
        phi = (1 + sqrt5)/2
        shi = (1 - sqrt5)/2
        return round((phi**(n+1) - shi**(n+1))/sqrt5)