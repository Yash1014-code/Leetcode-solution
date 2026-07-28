class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        left, right = 0, m * n - 1
        while left <= right:
            i = (left + right) // 2
            v = matrix[i // n][i % n]
            if v == target:
                return True
            elif v < target:
                left = i + 1
            else:
                right = i - 1
        return False  
