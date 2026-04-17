from functools import lru_cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+nums+[1]
        n = len(nums)

        @lru_cache(maxsize =None)
        def dfs(left,right):
            if left>right:
                return 0
            #if in cache return
            coins = 0
            for i in range(left,right+1):
                burst = nums[left-1]*nums[i]*nums[right+1]
                coins = max(coins,burst+dfs(left,i-1)+dfs(i+1,right))
            return coins

        
        res = dfs(1,n-2)
        dfs.cache_clear()
        return res

