class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        b, s = 0, 1

        while s < len(prices):
            if prices[s] <= prices[b]:
                b = s
            if prices[s] > prices[b]:
                profit = max(profit, prices[s] - prices[b])
            s = s + 1

        return profit