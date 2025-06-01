from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        if nums:
            ans = 1
        consecutive_length = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] - nums[i-1] == 1:
                consecutive_length+=1
            else:
                consecutive_length=1
            ans = max(ans, consecutive_length)
        return ans
