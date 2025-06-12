class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_map = {
            "[": "]",
            "(": ")",
            "{": "}"
        }
        for char in s:
            if stack and not hash_map.get(stack[-1]):
                return False
            if stack and hash_map.get(stack[-1]) == char:
                stack.pop()
            else:
                stack.append(char)
        if stack:
            return False
        return True
