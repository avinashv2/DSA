from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        row_filled = 0
        start, end = 0, len(height)-1
        while start < end:
            min_col = min(height[start], height[end])
            if row_filled < min_col:
                area += (end-start-1)*(min_col-row_filled)
                row_filled = min_col

            if height[start]<=height[end]:
                start+=1
                if start<end:
                    area-=min(row_filled,height[start])
            else:
                end-=1
                if start<end:
                    area-=min(row_filled,height[end])
        return area
