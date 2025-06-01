from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            num_to_add = target - num
            if num_to_add in hashmap:
                return [hashmap[num_to_add], index]
            hashmap[num] = index
