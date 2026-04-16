from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        prev = [0]*(m+1)

        for i in range(n):
            cur = [0]*(m+1)
            for j in range(m):

                if text1[i] == text2[j]:
                    cur[j+1] = 1 + prev[j]
                else:
                    cur[j+1] = max(prev[j+1], cur[j])
            prev = cur
        return prev[m]
    