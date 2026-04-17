from functools import lru_cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)

        @lru_cache(maxsize = None)
        def dfs(i,j):
            if i == n and j == m:     # if both i and j reach to end together means both strings match
                return True
            if j == m:                # if p reaches to and but s still has some characters in it
                return False
            if i == n:                # if s reaches to end, but p still has some characters left

                if j==m-1 and p[j]=="*":    #check of j stuck at last position(m-1) because of special char '*'
                    return True
                while j+1 < m and p[j+1]=="*":   #if j is not at m-1 but char next to j is "*" so we can consider p[j]* == ""
                    j+=2                         # skip all such possible combinations
                return False if j!=m else True   # if still some char left after removing all p[j]*, return false
            
            if j+1<m and p[j+1]=="*":   # if character p[j] is followed by a "*"
                match_choice = False
                
                skip_choice = dfs(i,j+2)        # p[j]* = ""     considering zero occurance of p[j], i stays still

                if s[i]==p[j] or p[j]==".":     # if p[j] is special char "." or equal to s[i]
                    match_choice = dfs(i+1,j)   # increment only i and check for multiple occurances of p[j]

                return (skip_choice or match_choice)  # atleast one of them is True


            if s[i]==p[j] or p[j]==".":   # if character p[j] is not followed by a "*"
                return dfs(i+1,j+1)       # increment both i and j
            return False
                    

        res = dfs(0,0)
        dfs.cache_clear()
        return res