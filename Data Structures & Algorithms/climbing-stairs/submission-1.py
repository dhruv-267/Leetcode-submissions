class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [-1]*n
        def climb(h): 
            if h>=n:
                return h==n
            
            if mem[h]!= -1:
                return mem[h]

            mem[h] = climb(h+1)+climb(h+2)
            return mem[h]
        return climb(0)
        