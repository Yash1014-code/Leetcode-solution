class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area=0

        def dfs(i,j):
            if min(i,j)<0 or i==rows or j==cols or grid[i][j]==0:
                return 0
            grid[i][j]=0
            return (1+ dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1))   

        for i in range(rows):
            for j in range(cols):
                    max_area = max(max_area,dfs(i,j))
        return max_area            
