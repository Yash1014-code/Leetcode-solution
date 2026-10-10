class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        for i in range(0,row):
            for j in range(0,col):
                if target==matrix[i][j]:
                    return True
        return False
