from functools import lru_cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)

        @lru_cache(maxsize = None)
        def dfs(i,j):
            if i == n and j == m:
                return True
            if j == m:
                return False
            if i == n:
                if j==m-1 and p[j]=="*":
                    return True
                while j+1 < m and p[j+1]=="*":
                    j+=2
                return False if j!=m else True
            
            if j+1<m and p[j+1]=="*":
                match = False
                skip = dfs(i,j+2) # a* = ""
                if s[i]==p[j] or p[j]==".":
                    match = dfs(i+1,j)
                return (skip or match)
            if s[i]==p[j] or p[j]==".":
                return dfs(i+1,j+1)
            return False
                    

        res = dfs(0,0)
        dfs.cache_clear()
        return res