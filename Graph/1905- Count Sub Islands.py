class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        rows = len(grid2)
        cols = len(grid2[0])
        count=0
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        def dfs(i,j):
            if i<0 or j<0 or i>=rows or j>=cols or grid2[i][j]==0:
                return True
            grid2[i][j]=0
            is_sub = (grid1[i][j]==1)
            for dr,dc in dirs :
                if not dfs(i+dr,j+dc): is_sub = False
            return is_sub    


        for i in range(rows):
            for j in range(cols):
                if grid2[i][j]==1: 
                    if dfs(i,j):
                        count+=1
        return count                
