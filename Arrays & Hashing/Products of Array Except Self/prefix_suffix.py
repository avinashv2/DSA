from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [0]*len(nums)
        prefix_product[0] = nums[0]
        suffix_product = [0]*len(nums)
        suffix_product[-1] = nums[-1]
        for i in range(1,len(nums)):
            prefix_product[i] = prefix_product[i-1]*nums[i]

        for i in range(len(nums)-2,-1, -1):
            suffix_product[i] = suffix_product[i+1]*nums[i]

        ans = []
        for i in range(len(nums)):
            product = 1
            if i > 0:
                product*=prefix_product[i-1]
            if i < (len(nums)-1):
                product*=suffix_product[i+1]
            ans.append(product)
        return ans
