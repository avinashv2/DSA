from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        prefix = [0]*len(nums)
        suffix = [0]*len(nums)
        limit = len(nums)
        for i, num in enumerate(nums):
            if i%k == 0:
                prefix[i] = num
            else:
                prefix[i] = max(prefix[i-1], num)

            if (limit-i)%k == 0 or i == 0:
                suffix[limit-i-1] = nums[limit-i-1]
            else:
                suffix[limit-i-1] = max(suffix[limit-i], nums[limit-i-1])
        output = [0]*(limit-(k-1))
        for i in range(len(output)):
            output[i] = max(prefix[(k-1)+i], suffix[i])
        return output

