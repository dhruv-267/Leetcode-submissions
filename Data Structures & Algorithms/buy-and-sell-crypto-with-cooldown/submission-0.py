from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0

        @lru_cache(maxsize =None)
        def dfs(i,buy):
            if i >= n :
                return profit
            if buy:
                return max(dfs(i+1,False) - prices[i] , dfs(i+1,True))
            else:
                return max(dfs(i+1,buy),dfs(i+2,True) + prices[i]-buy)
        res = dfs(0,True)
        dfs.cache_clear()
        return res