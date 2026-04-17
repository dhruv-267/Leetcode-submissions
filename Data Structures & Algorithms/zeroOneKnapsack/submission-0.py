from functools import lru_cache
class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        @lru_cache(maxsize = None)
        def knp(i,capacity):
            if i == n:
                return 0
            
            maxprofit = knp(i+1,capacity)

            if weight[i]<=capacity:
                p = profit[i] + knp(i+1,capacity-weight[i])
                maxprofit = max(maxprofit,p)
            
            return maxprofit
        res =  knp(0,capacity)
        knp.cache_clear()
        return res
