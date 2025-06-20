from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [1]*len(nums)
        for i in range(1,len(nums)):
            prefix_product[i] = prefix_product[i-1]*nums[i-1]
        infix = 1
        for i in range(len(nums)-1, -1, -1):
            prefix_product[i] *= infix
            infix*=nums[i]
        return prefix_product
