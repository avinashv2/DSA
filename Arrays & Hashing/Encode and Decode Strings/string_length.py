from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for string in strs:
            s += str(len(string))+"#"+string
        return s

    def decode(self, s: str) -> List[str]:
        print(s)
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1

            length = int(s[i:j])
            ans.append(s[j+1:j+length+1])
            i = j+1+length
        return ans
