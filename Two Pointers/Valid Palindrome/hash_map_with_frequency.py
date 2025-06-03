from typing import List
from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        freq = defaultdict(int)

        for num in nums:
            freq[num] +=1

        for i, num in enumerate(nums):
            freq[num] -= 1
            if i>0 and num == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                freq[nums[j]] -= 1
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                find = -(num + nums[j])
                if freq[find]>0:
                    result.append([num, nums[j], find])
            for j in range(i + 1, len(nums)):
                freq[nums[j]] += 1
        return result 