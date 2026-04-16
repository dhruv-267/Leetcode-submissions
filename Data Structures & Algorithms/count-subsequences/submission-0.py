from functools import lru_cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        @lru_cache(maxsize = None)
        def ds(i,j):
            if j == m:
                return 1
            if i == n:
                return 0
            if s[i]==t[j]:
                return ds(i+1,j+1) + ds(i+1,j)
            else:
                return ds(i+1,j)
        res =  ds(0,0)
        ds.cache_clear()
        return res