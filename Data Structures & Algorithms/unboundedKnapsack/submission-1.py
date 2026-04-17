from functools import lru_cache
class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        
        prev = [0]*(capacity+1)

        for i in range(len(profit)):
            cur = [0]*(1+capacity)
            for j in range(1+capacity):
                skip = prev[j]
                p=0
                if weight[i]<=j:
                    p = profit[i] + cur[j-weight[i]]
                cur[j] = max(skip,p)
            prev = cur
        return prev[-1]     
        
        '''
        n = len(profit)
        @lru_cache(maxsize = None)
        def knp(i,capacity):
            if i == n:
                return 0
            
            maxprofit = knp(i+1,capacity)

            if weight[i]<=capacity:
                p = profit[i] + knp(i,capacity-weight[i])
                maxprofit = max(maxprofit,p)
            
            return maxprofit
        res =  knp(0,capacity)
        knp.cache_clear()
        return res
        '''