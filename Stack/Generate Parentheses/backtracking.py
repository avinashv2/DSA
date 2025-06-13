from typing import List
from collections import defaultdict

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        state = defaultdict(int)
        stack = []

        def backtracking():
            if state["("]<n:
                state["("]+=1
                stack.append("(")
                backtracking()
                stack.pop()
                state["("]-=1
            if state[")"] < state["("]:
                state[")"]+=1
                stack.append(")")
                backtracking()
                stack.pop()
                state[")"]-=1

            if len(stack) == n*2:
                res.append("".join(stack))
                return

        backtracking()
        return res

