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
            arr.append([value, key])
        arr.sort(key=lambda x: x[0])
        start = (len(arr))-k
        for i in range(start, len(arr)):
            result.append(arr[i][1])
        return result