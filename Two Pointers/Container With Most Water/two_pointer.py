from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        start, end = 0, len(heights)-1

        while start < end:
            container_max = min(heights[start], heights[end])
            res = max(res, (end-start)*container_max)
            if heights[start] <= heights[end]:
                start+=1
                continue
            end-=1
        return res
