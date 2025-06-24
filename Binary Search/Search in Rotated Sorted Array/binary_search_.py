from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        while start<=end:
            mid = start+((end-start)//2)
            if nums[mid]==target:
                return mid
            
            if nums[start]<=nums[mid]:
                if target<nums[start] or target>nums[mid]:
                    start = mid+1
                else:
                    end = mid-1
            else:
                if target < nums[mid] or target>nums[end]:
                    end = mid-1
                else:
                    start = mid+1
        return -1
