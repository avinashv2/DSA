from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        ans = 0
        for num in hash_set:
            if num-1 in hash_set:
                continue
            consecutive_length = 1
            while num+consecutive_length in hash_set:
                consecutive_length+=1
            ans = max(consecutive_length, ans)
        return ans
