class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {0:1,1:1}
        def dfs(i,cache):
            if i<0:
                return 0
            if i in cache:
                return cache[i]

            cache[i] = dfs(i-1,cache)+dfs(i-2,cache)
            return cache[i]
        return dfs(n,cache)