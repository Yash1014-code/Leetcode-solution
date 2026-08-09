class Solution:
    def dfs(self,r,c,visited,rows,cols,board):
        if r<0 or r>=rows or c<0 or c>=cols:
            return
        if board[r][c]=="X":
            return
        if visited[r][c]==1:
            return
        visited[r][c]=1
        self.dfs(r-1,c,visited,rows,cols,board)
        self.dfs(r,c-1,visited,rows,cols,board)
        self.dfs(r,c+1,visited,rows,cols,board)
        self.dfs(r+1,c,visited,rows,cols,board)


    def solve(self, board: List[List[str]]) -> None:
        rows= len(board)
        cols=len(board[0])
        visited=[[0 for _ in range(cols)]for _ in range(rows)]
        # upper row
        r,c=0,0
        for c in range(cols):
            if board[r][c]=="O":
                if visited[r][c]==0:
                    self.dfs(r,c,visited,rows,cols,board)
        #last row
        r,c=rows-1,0
        for c in range(cols):
            if board[r][c]=="O":
                if visited[r][c]==0:
                    self.dfs(r,c,visited,rows,cols,board)
        # first cols
        r,c=0,0
        for r in range(rows):
            if board[r][c]=="O":
                if visited[r][c]==0:
                    self.dfs(r,c,visited,rows,cols,board)
        #last cols
        r,c=0,cols-1
        for r in range(rows):
            if board[r][c]=="O":
                if visited[r][c]==0:
                    self.dfs(r,c,visited,rows,cols,board) 
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O"and visited[r][c]==0:
                    board[r][c]="X"            
