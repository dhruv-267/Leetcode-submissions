from functools import lru_cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        c = len(coins)

        @lru_cache(maxsize = None)
        def dfs(i,amt):
            if amt==0:
                return 1
            if amt<0 or i==c:
                return 0
            return dfs(i,amt-coins[i])+dfs(i+1,amt)
        res = dfs(0,amount)
        dfs.cache_clear()
        return res

            
