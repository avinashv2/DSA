from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        start, end = 0, len(height)-1
        leftmax = height[start]
        rightmax = height[end]
        while start < end:
            while start < end and height[start] > height[end]:
                rightmax = max(rightmax, height[end])
                res+= rightmax-height[end]
                end-=1
            while start < end and height[start] <= height[end]:
                leftmax = max(leftmax, height[start])
                res+= leftmax-height[start]
                start+=1
        return res
            

