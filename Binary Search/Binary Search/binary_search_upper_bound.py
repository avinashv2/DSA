from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start = 0
        end = n
        while start<end:
            mid = start+((end-start)//2)
            if nums[mid]>target:
                end = mid
            if nums[mid]<=target:
                start = mid+1
        return start-1 if (start and nums[start-1] == target) else -1
