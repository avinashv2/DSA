from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": self.add,
            "-": self.sub,
            "*": self.mul,
            "/": self.div
        }
        def dfs():
            token = tokens.pop()
            if token not in ops:
                return int(token)
            
            right = dfs()
            left = dfs()

            return int(ops[token](left, right))

        
        return dfs()
    def add(self, a, b):
        return a+b
    def sub(self, a, b):
        return a-b
    def mul(self, a, b):
        return a*b
    def div(self, a, b):
        return a/b