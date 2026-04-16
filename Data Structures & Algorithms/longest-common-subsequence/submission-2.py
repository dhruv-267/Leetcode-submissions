from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        
        @lru_cache(maxsize=None)
        def LCS(i,j):
            if i == n or j==m:
                return 0
            if text1[i]==text2[j]:
                return 1 + LCS(i+1,j+1)
            else:
                return max(LCS(i+1,j),LCS(i,j+1))
        res = LCS(0,0)
        LCS.cache_clear()
        return res