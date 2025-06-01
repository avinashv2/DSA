import heapq
from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        result = []
        for num in nums:
            freq[num] +=1
        arr = []
        for key, value in freq.items():
            heapq.heappush(arr, [value, key])
            if len(arr) > k:
                heapq.heappop(arr)
        for i in range(len(arr)):
            result.append(heapq.heappop(arr)[1])
        return result
