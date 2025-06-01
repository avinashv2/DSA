from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        zero_index = -1
        for i,num in enumerate(nums):
            if num == 0:
                zero_count+=1
                zero_index = i
            else:
                product*=num
        if zero_count > 1:
            return [0]*len(nums)
        if zero_count == 1:
            arr = [0]*len(nums)
            arr[zero_index] = product
            return arr
        arr = [0]*len(nums)
        for i, num in enumerate(nums):
            arr[i] = product//num
        return arr
