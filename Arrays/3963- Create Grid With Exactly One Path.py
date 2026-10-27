class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [["#"]*n for i in range(m) ]
        i, j = 0, 0
        while j<n:
            grid[0][j]="."
            j+=1
        while i<m:
            grid[i][n-1]="."
            i+=1   
        return["".join(row) for row in grid]     
