from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []
        stack = []
        for i, pos in enumerate(position):
            pos_speed.append((pos, speed[i]))
        pos_speed.sort()
        for i, ps in enumerate(pos_speed):
            while stack and stack[-1][1]>ps[1] and (target-stack[-1][0])/stack[-1][1]<=(target-ps[0])/ps[1]:
                stack.pop()
            stack.append(ps)
        return len(stack)