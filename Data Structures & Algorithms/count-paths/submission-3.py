from functools import lru_cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        postrow = [1]*n
        for row in range(m-2,-1,-1):
            currow = [0]*n
            currow[n-1] = 1
            for col in range(n-2,-1,-1):
                currow[col] = currow[col+1]+postrow[col]
            postrow=currow 
        return postrow[0]