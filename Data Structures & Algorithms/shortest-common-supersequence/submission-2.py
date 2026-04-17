from functools import lru_cache
class Solution:

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        n = len(str1)
        m = len(str2)
        
        prev = [""]*(m+1)
        for j in range(m):
            prev[j] = str2[j:]
        
        for i in range(n-1,-1,-1):
            cur = [""]*(m+1)
            cur[-1] = str1[i:]
            for j in range(m-1,-1,-1):

                if str1[i] == str2[j]:
                    cur[j] = str2[j] + prev[j+1]
                else:
                    s1 = str1[i]+prev[j]
                    s2 = str2[j]+cur[j+1]
                    cur[j] = s1 if len(s1)<len(s2) else s2
            prev = cur
        
        return prev[0]


        
        
        
        '''
        n = len(str1)
        m = len(str2)

        @lru_cache(maxsize = None)
        def dfs(i,j):
            if i == n:
                return str2[j:]
            if j == m:
                return str1[i:]
            if str1[i]==str2[j]:
                return str1[i]+dfs(i+1,j+1)
            else:
                s1 = str1[i]+dfs(i+1,j)
                s2 = str2[j]+dfs(i,j+1)
                return s1 if len(s1)<len(s2) else s2
        
        res = dfs(0,0)
        dfs.cache_clear()
        return res
        '''