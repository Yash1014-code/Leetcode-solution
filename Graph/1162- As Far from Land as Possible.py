class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        n = len(grid)
        dist = 0
        q = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    q.append((i,j))
        if len(q) == n*n:
            return -1            
        while q:
            size = len(q)
            dist+=1
            for _ in range(size):
                r, c = q.popleft()
                for i,j in [(0,1), (1,0), (-1,0), (0,-1)]:
                    nr, nc = i+r, j+c
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        q.append((nr,nc))
        return dist-1  
