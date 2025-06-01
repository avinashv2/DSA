class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a = list(s)
        b = list(t)
        a.sort(key=lambda x: ord(x))
        b.sort(key=lambda x: ord(x))
        return a == b
