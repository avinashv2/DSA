class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = s.lower()
        start = 0
        end = len(text)-1
        while start <= end:
            while start <= end and not text[start].isalnum():
                start+=1
            while start <= end and not text[end].isalnum():
                end-=1
            if start <= end and text[start] != text[end]:
                return False
            start+=1
            end-=1
        return True
