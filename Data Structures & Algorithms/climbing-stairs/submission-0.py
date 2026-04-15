class Solution:
    def climbStairs(self, n: int,cache={}) -> int:
        cache = {}
        def dsf(i,cache):
            if i == n:
                return 1
            if i>n:
                return 0 
            if i in cache:
                return cache[i]
            cache[i] = dsf(i+1,cache)+dsf(i+2,cache)
            return cache[i]
        
        return dsf(0,{})
