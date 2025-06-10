from typing import List
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        res.append(-heap[0][0])
        l=0
        for i in range(k, len(nums)):
            l+=1
            heapq.heappush(heap, (-nums[i], i))
            while heap[0][1]<l:
                heapq.heappop(heap)
            res.append(-heap[0][0])
        return res
