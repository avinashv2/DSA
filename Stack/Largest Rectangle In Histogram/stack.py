from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        n = len(heights)
        prefix = [-1]*n
        stack = []
        for i, height in enumerate(heights):
            while stack and heights[stack[-1]]>=height:
                stack.pop()
            if stack:
                prefix[i] = stack[-1]
            stack.append(i)
        suffix = [n]*n
        stack = []
        for i in range(len(heights)-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                suffix[i] = stack[-1]
            stack.append(i)
        for i, height in enumerate(heights):
            ans = max(ans, (suffix[i]-prefix[i]-1)*height)
        return ans
