from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)-1
        row, col = 0, len(matrix[0])-1

        while row<=m and col>=0:
            if matrix[row][col]<target:
                row+=1
            elif matrix[row][col]>target:
                col-=1
            elif matrix[row][col]==target:
                return True
        return False
