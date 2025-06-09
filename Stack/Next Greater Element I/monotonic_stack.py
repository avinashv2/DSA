from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        position = {}
        for i, num in enumerate(nums2):
            position[num] = i
        
        nge = [-1]*len(nums2)
        stack = []
        stack.append(nums2[-1])
        for i in range(len(nums2)-2, -1, -1):

            while stack and nums2[i]>=stack[-1]:
                stack.pop()
            
            if stack:
                nge[i] = stack[-1]
            stack.append(nums2[i])
        res = []
        for num in nums1:
            res.append(nge[position[num]])
        return res
