from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num_1 in enumerate(nums):
            for j in range(i+1, len(nums)):
                if num_1 + nums[j] == target:
                    return [i, j]
