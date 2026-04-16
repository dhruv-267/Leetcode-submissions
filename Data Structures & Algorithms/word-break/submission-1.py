class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True

        for i in range(n-1,-1,-1):
            for w in wordDict:
                wordlen = len(w)
                if ( i + wordlen -1 < n) and s[ i : i+wordlen ] == w:
                    dp[i]=dp[i+wordlen]
                if dp[i]:
                    break
        
        return dp[0]