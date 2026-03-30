class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0,1
        profit = 0
        while sell < len(prices) :
            if prices[sell] < prices[buy]:
                buy = sell
                sell += 1
            else:
                profit = max(profit,prices[sell]-prices[buy])
                sell += 1
        return profit

        