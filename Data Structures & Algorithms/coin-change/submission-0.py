class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = { i:math.inf for i in range(amount+1)}
        dp[0] = 0

        for i in range(amount+1):
            for c in coins:
                if i-c>=0:
                    dp[i] = min(dp[i],1 + dp[i-c])
        return dp[amount] if dp[amount]!=math.inf else -1