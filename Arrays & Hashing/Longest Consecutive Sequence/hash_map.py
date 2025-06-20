from typing import List
from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1

                mp[num - mp[num-1]] = mp[num]
                mp[num + mp[num+1]] = mp[num]
            res = max(mp[num], res)
        return res
