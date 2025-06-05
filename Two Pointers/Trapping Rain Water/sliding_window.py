from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        start = 0
        temp = 0
        for i in range(1, len(height)):
            if height[start] <= height[i]:
                area += height[start]*(i-start-1)
                area -= temp
                temp = 0
                start = i
            else:
                temp+=height[i]
        start = len(height)-1
        temp = 0
        for i in range(len(height)-2, -1, -1):
            if height[start] < height[i]:
                print(height[start], height[i])
                area += height[start]*(start-i-1)
                area -= temp
                temp = 0
                start = i
            else:
                temp+=height[i]
        
        return area
