from functools import lru_cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n + m != len(s3):
            return False

        @lru_cache(maxsize=None)
        def inter(i,j):
            if i==n and j==m:
                return True
            if i<n and s1[i]==s3[i+j] and inter(i+1,j):
                return True
            if j<m and s2[j]==s3[i+j] and inter(i,j+1):
                return True
            return False
        res = inter(0,0)
        inter.cache_clear()
        return res