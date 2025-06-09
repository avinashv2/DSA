class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = None
        min_len = float("+inf")
        t_freq = [0]*128
        for i, char in enumerate(t):
            t_freq[ord(char)]+=1
        
        for i in range(len(s)):
            s_freq = [0]*128
            for j in range(i, len(s)):
                s_freq[ord(s[j])]+=1
                if self.check(t_freq, s_freq) and min_len > (j-i+1):
                    min_len = j-i+1
                    ans = (i, j)
        if ans:
            return s[ans[0]:ans[1]+1]
        return ""
    def check(self, t, s):
        for i in range(128):
            if t[i] > s[i]:
                return False
        return True
