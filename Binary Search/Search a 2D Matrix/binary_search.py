from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        m_n = m*n
        start, end =0, m_n-1

        while start<=end:
            mid = start+((end-start)//2)
            row = mid//n
            column = mid%n
            if matrix[row][column] == target:
                return True
            if matrix[row][column]>target:
                end = mid-1
            if matrix[row][column]<target:
                start = mid+1
        return False
