from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        res = [0]*n
        for i in range(len(temperatures)-2, -1, -1):
            j = i+1
            while j<n and temperatures[i] >= temperatures[j]:
                if res[j] == 0:
                    break
                j += res[j]
            if temperatures[i] < temperatures[j]:
                res[i] = j-i
        return res