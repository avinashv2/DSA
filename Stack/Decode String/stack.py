class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        start = 0
        while start < len(s):
            digit = ""
            while s[start].isdigit():
                digit+=s[start]
                start+=1
            if digit:
                stack.append(digit)
            print(stack)
            print(start)
            if s[start] == "[":
                stack.append(s[start])
                start+=1
            temp_str=""
            while start < len(s) and s[start].isalpha():
                temp_str+=s[start]
                start+=1
            if temp_str:
                stack.append(temp_str)
            print(stack)
            temp_res = ""
            if start < len(s) and s[start] == "]":
                while stack[-1] != "[":
                    temp_res=stack.pop()+temp_res
                    print(temp_res)
                stack.pop()
                num = int(stack.pop())
                stack.append(temp_res*num)
                start+=1
        return "".join(stack)
