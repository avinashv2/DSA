from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []
        for i, pos in enumerate(position):
            pos_speed.append((pos, speed[i]))
        pos_speed.sort(reverse=True)
        time_pointer = 0
        ans = 0
        for i,(pos, s) in enumerate(pos_speed):
            time = (target-pos)/s
            if i==0 or time > time_pointer:
                time_pointer = time
                ans+=1
        return ans