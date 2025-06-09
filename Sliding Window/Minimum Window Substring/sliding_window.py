from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        l = 0
        s_freq, t_freq = defaultdict(int), defaultdict(int)
        need = len(t)
        for char in t:
            t_freq[char] +=1
        min_len = float('+inf')
        matches = 0
        for r, char in enumerate(s):
            s_freq[char] += 1
            if s_freq[char] <= t_freq[char]:
                matches+=1
            while matches == need:
                if r-l+1 < min_len:
                    res = s[l:r+1]
                    min_len = r-l+1
                s_freq[s[l]]-=1
                if s_freq[s[l]] < t_freq[s[l]]:
                    matches-=1
                l+=1
        return res
