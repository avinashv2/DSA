from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        prefix_highest = [0]*len(height)
        prefix_highest_point = 0
        suffix_highest_point = 0
        for i in range(len(height)):
            prefix_highest_point = max(prefix_highest_point, height[i])
            prefix_highest[i] = prefix_highest_point
        
        for i in range(len(height)-1, -1, -1):
            suffix_highest_point = max(suffix_highest_point, height[i])
            min_col = min(suffix_highest_point, prefix_highest[i])
            if min_col > height[i]:
                area += min_col - height[i]

        return area
