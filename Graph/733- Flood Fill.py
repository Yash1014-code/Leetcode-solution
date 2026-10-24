class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color:
            return image
        visited=deepcopy(image)
        rows=len(visited)
        cols=len(visited[0])
        ini_color=image[sr][sc]
        self.dfs(sr,sc,color,visited,ini_color,rows,cols)    
        return visited
    def dfs(self,i,j,color,visited,ini_color,rows ,cols):
        if i<0 or i>=rows or j<0 or j>=cols:
            return 
        if visited[i][j]!= ini_color:
            return
        if visited[i][j]==ini_color:
            visited[i][j]=color
        self.dfs(i+1,j,color,visited,ini_color,rows,cols) 
        self.dfs(i,j+1,color,visited,ini_color,rows,cols) 
        self.dfs(i-1,j,color,visited,ini_color,rows,cols) 
        self.dfs(i,j-1,color,visited,ini_color,rows,cols) 
