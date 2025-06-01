from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        result = []
        for num in nums:
            freq[num] +=1
        bucket = [[] for i in range(len(nums))]

        for key, value in freq.items():
            bucket[value-1].append(key)
        start = len(nums)-1

        while k>0 and start>=0:
            for i in bucket[start]:
                if k <=0:
                    break
                result.append(i)
                k-=1
            start-=1
        return result
