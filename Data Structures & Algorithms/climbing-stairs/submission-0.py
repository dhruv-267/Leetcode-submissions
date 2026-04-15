class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {n:1}
        def dfs(i,cache):
            if i>n:
                return 0
            if i in cache:
                return cache[i]

            cache[i] = dfs(i+1,cache) + dfs(i+2,cache)
            return cache[i]
        return dfs(0,cache)