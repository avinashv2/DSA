import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        ans = max(piles)
        start, end = 1, max(piles)

        while start<=end:
            mid = start+((end-start)//2)
            if self.check(mid, piles, h):
                end = mid-1
                ans = mid
            else:
                start=mid+1
        return ans
    
    def check(self, mid, piles, h):
        temp = 0
        for i in range(len(piles)-1, -1, -1):
            temp+=math.ceil(piles[i]/mid)
            if temp > h:
                return False
        return True