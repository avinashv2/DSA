from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end =0, len(nums)-1
        while start<=end:
            if start == end:
                return nums[start]
            mid = start+((end-start)//2)
            if nums[start]>nums[mid]:
                end = mid
            elif nums[mid]>nums[end]:
                start = mid+1
            elif nums[mid]<nums[mid+1]:
                end = mid
            elif nums[mid]>nums[mid+1]:
                start = mid+1
        return nums[start]
