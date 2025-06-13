from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            "+": self.add,
            "-": self.sub,
            "*": self.mul,
            "/": self.div
        }
        for i, token in enumerate(tokens):
            if token in ops:
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(ops[token](a,b))
            else:
                stack.append(token)
        return int(stack[0])
    def add(self, a, b):
        return a+b
    def sub(self, a, b):
        return a-b
    def mul(self, a, b):
        return a*b
    def div(self, a, b):
        return a/b