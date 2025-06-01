from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0]*9
        cols = [0]*9
        cubes = [0]*9

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                pos = int(board[i][j]) - 1
                if (1<<pos) & rows[i]:
                    return False
                if (1<<pos) & cols[j]:
                    return False
                if (1<<pos) & cubes[(i//3)*3 + j//3]:
                    return False
                rows[i] |= 1<<pos
                cols[j] |= 1<<pos
                cubes[(i//3)*3 + j//3] |= 1<<pos
        return True
