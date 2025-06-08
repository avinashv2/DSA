class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        s1_f = [0]*26
        s2_f = [0]*26
        for i, char in enumerate(s1):
            s1_f[ord(char)-ord('a')] += 1
        l=0
        for r, char in enumerate(s2):
            s2_f[ord(char)-ord('a')] +=1
            if r-l+1 == window:
                if s1_f == s2_f:
                    return True
                s2_f[ord(s2[l])-ord('a')] -=1
                l+=1
        return False
