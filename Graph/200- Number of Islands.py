class Solution:
    def bfs(self,i,j,visited,grid):
        row=len(grid)
        col=len(grid[0])
        queue=deque()
        queue.append((i,j))
        visited[i][j]=1
        while len(queue)!=0:
            x,y=queue.popleft()
            for p,q in [(-1,0),(0,-1),(0,1),(1,0)]:
                new_x,new_y=x+p,y+q
                if new_x<0 or new_y<0 or new_x>=row or new_y>=col:
                    continue
                if grid[new_x][new_y]=="0" :
                    continue
                if visited[new_x][new_y]==1:
                    continue 
                visited[new_x][new_y]=1
                queue.append((new_x,new_y))
    def numIslands(self, grid: List[List[str]]) -> int:
        row=len(grid)
        col=len(grid[0])
        visited=[[0 for _ in range(col)] for _ in range(row)]
        count=0
        for r in range(row):
            for c in range(col):
                if grid[r][c]=="1" and visited[r][c]==0:
                    count+=1
                    self.bfs(r,c,visited,grid)
        return count            
