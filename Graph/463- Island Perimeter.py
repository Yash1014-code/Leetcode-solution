class Solution:
    def dfs(self,grid,i,j,n,m):
        if i<0 or i>=n or j<0 or j>=m or grid[i][j]==0:
            self.peri+=1
            return 
        if grid[i][j] == -1: 
            return 
        grid[i][j] = -1 

        self.dfs(grid,i+1,j,n,m)
        self.dfs(grid,i,j+1,n,m)
        self.dfs(grid,i,j-1,n,m)
        self.dfs(grid,i-1,j,n,m)
        

    def islandPerimeter(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        self.peri = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    self.dfs(grid,i,j,n,m)
                    return self.peri
        return -1         
