from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, num in enumerate(nums):
            l = i+1
            r = len(nums)-1
            if i>0 and num == nums[i-1]:
                continue
            while l<r:
                v = num + nums[l] + nums[r]
                if v > 0:
                    r-=1
                elif v < 0:
                    l+=1
                else:
                    result.append([num,nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
        return result
