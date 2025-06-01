from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            s = set()
            for j in range(len(board)):
                if board[i][j] != ".":
                    if board[i][j] not in s:
                        s.add(board[i][j])
                    else:
                        return False
        for i in range(len(board)):
            s = set()
            for j in range(len(board)):
                if board[j][i] != ".":
                    if board[j][i] not in s:
                        s.add(board[j][i])
                    else:
                        return False 
        for i in range(len(board)):
            s = set()
            start = 3*(i//3)
            end = start+3
            start_ = (i%3)*3
            end_ = start_+3
            for j in range(start_, end_):
                for k in range(start, end):
                    if board[j][k] != ".":
                        if board[j][k] not in s:
                            s.add(board[j][k])
                        else:
                            return False
        return True
