from functools import lru_cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        @lru_cache(maxsize=None)
        def dist(i,j):
            if i==n:
                return m - j
            if j==m:
                return n - i
            
            if word1[i]==word2[j]:
                return dist(i+1,j+1)
            else:
                return min(1 + dist(i,j+1), 1 + dist(i+1,j),1 + dist(i+1,j+1))
            
        res = dist(0,0)
        dist.cache_clear()
        return res
