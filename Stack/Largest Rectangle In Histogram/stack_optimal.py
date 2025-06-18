from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        ans = 0
        for i, height in enumerate(heights):
            a = i
            while stack and stack[-1][0]>=height:
                h, pos = stack.pop()
                print(h, pos)
                print((i-pos)*h)
                ans = max(ans, (i-pos)*h)
                a=pos
            stack.append((height, a))
        
        while stack:
            height, pos = stack.pop()
            ans = max(ans, (n-pos)*height)
        
        return ans