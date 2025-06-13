class MinStack:
    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val-self.min)
            self.min = min(val, self.min)

    def pop(self) -> None:
        if self.stack:
            pop = self.stack.pop()
            if pop<0:
                self.min = self.min - pop

    def top(self) -> int:
        if self.stack[-1]<0:
            return self.min
        else:
            return self.stack[-1]+self.min

    def getMin(self) -> int:
        return self.min
