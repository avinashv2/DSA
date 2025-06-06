
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        ans = 0
        l = 0
        for r, char in enumerate(s):
            if char in hashmap:
                l = max(l, hashmap[char] + 1)
            hashmap[char] = r
            ans = max(ans, r-l +1)
        return ans
