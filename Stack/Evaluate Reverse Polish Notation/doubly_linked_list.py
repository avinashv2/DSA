from typing import List

class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": self.add,
            "-": self.sub,
            "*": self.mul,
            "/": self.div
        }
        head = Node(tokens[0])
        for i in range(1, len(tokens)):
            if tokens[i] in ops:
                head.val = ops[tokens[i]](
                    int(head.prev.val),
                    int(head.val))
                head.prev = head.prev.prev
            else:
                print(head.val)
                head.next = Node(tokens[i])
                head.next.prev = head
                head = head.next
                print(head.val)
        return int(head.val)

    def add(self, a, b):
        return a+b
    def sub(self, a, b):
        return a-b
    def mul(self, a, b):
        return a*b
    def div(self, a, b):
        return a/b