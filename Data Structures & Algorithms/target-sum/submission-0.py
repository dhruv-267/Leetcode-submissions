from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total = 0
        @lru_cache(maxsize=None)
        def dfs(i,total):
            if i == n and total == target:
                return 1
            if i==n:
                return 0
            return dfs(i+1,total+nums[i]) + dfs(i+1,total-nums[i])
        
        res = dfs(0,0)
        dfs.cache_clear()
        return res
            

