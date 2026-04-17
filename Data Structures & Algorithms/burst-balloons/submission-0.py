from functools import lru_cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + [x for x in nums] + [1]
        n = len(nums)

        @lru_cache(maxsize = None)
        def dfs(left, right):
            if left + 1 == right:
                return 0
            
            coins = 0
            for i in range(left + 1, right):
                burst = nums[left] * nums[i] * nums[right]
                coins = max(coins, burst + dfs(left, i) + dfs(i, right))
            return coins
                
        res = dfs(0, n - 1)
        dfs.cache_clear()
        return res