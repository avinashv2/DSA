from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = defaultdict(int)
        ans = 0
        lar = 0
        start = 0
        for i, char in enumerate(s):
            hashmap[char]+=1
            lar+=1
            while hashmap[char] > 1:
                hashmap[s[start]]-=1
                lar-=1
                start+=1
            ans = max(ans, lar)
        return ans