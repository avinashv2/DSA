from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        window_start = 0
        for i in range(1, len(prices)):
            if prices[window_start] < prices[i]:
                ans = max(ans, prices[i]-prices[window_start])
            else:
                window_start = i
        return ans
