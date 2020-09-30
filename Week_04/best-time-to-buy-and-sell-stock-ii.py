class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, i = 0, 1
        while i < len(prices):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i - 1]
            i += 1
        return max_profit

    def maxProfit1(self, prices: List[int]) -> int:
        i, valley, peak, max_profit = 0, prices[0], prices[0], 0

        n = len(prices)
        while i < n - 1:
            while i < n - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]
            while i < n - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            max_profit += peak - valley
        return max_profit

    def maxProfit2(self, prices: List[int]) -> int:
        return sum([tomorrow - today for today, tomorrow in zip(prices, prices[1:]) if tomorrow - today > 0])

    def maxProfit3(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            profit += max(prices[i] - prices[i - 1], 0)
        return profit