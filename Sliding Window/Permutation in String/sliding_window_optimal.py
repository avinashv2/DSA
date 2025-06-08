class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_f = [0]*26
        s2_f = [0]*26
        matches = 0
        if len(s1)>len(s2):
            return False
        for i, char in enumerate(s1):
            s1_f[ord(char)-ord('a')] += 1
            s2_f[ord(s2[i])-ord('a')] += 1
        for i in range(26):
            matches += 1 if s1_f[i] == s2_f[i] else 0
        l=0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            index = ord(s2[l])-ord('a')
            s2_f[index]-=1
            if s2_f[index] == s1_f[index]:
                matches+=1
            if s2_f[index]+1 == s1_f[index]:
                matches-=1
            index = ord(s2[r])-ord('a')
            s2_f[index]+=1
            if s2_f[index] == s1_f[index]:
                matches+=1
            if s2_f[index]-1 == s1_f[index]:
                matches-=1
            l+=1
        return matches == 26
