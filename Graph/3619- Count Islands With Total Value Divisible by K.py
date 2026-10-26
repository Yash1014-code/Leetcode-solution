class Solution:
    def dfs(self,grid,i,j,n,m):
        if i<0 or j<0 or i>= n or j>=m:
            return 0
        if grid[i][j]==0:
            return 0
        count = grid[i][j]
        grid[i][j] = 0
        count+=self.dfs(grid,i+1,j,n,m)
        count+=self.dfs(grid,i,j+1,n,m)        
        count+=self.dfs(grid,i-1,j,n,m)        
        count+=self.dfs(grid,i,j-1,n,m)
        return count        

    def countIslands(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    ans = self.dfs(grid,i,j,n,m)
                    if ans%k == 0:
                        res+=1
        return res 
