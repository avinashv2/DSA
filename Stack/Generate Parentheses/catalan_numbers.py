class Solution:
    def generateParenthesis(self, n):
        res = [[] for i in range(n+1)]
        res[0] = [""]

        for i in range(1, n+1):
            for j in range(i):
                for a in res[j]:
                    for b in res[i-j-1]:
                        res[i].append(
                            "("+a+")"+b
                        )

        return res[-1]