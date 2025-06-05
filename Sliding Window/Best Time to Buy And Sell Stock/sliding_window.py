from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        start = float("+inf")
        for i in range(len(prices)):
            start = min(start, prices[i])
            profit = max(profit, prices[i] - start)
        return profit
