from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = []
        res = []
        l = 0
        pos = 0
        for r in range(len(nums)):
            while stack and nums[stack[-1]] < nums[r]:
                stack.pop()
                if pos!=0 and pos == len(stack)+1:
                    pos-=1
            stack.append(r)
            if r-l+1 == k:
                res.append(nums[stack[pos]])
                if l==stack[pos]:
                    pos+=1
                l+=1
        return res
