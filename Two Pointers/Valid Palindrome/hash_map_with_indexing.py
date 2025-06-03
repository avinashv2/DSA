from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        hash_map = {}

        for i, num in enumerate(nums):
            hash_map[num] = i

        for i, num in enumerate(nums):
            if i>0 and num == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                find = -(num + nums[j])
                if find in hash_map and hash_map[find]>j:
                    result.append([num, nums[j], find])

        return result 