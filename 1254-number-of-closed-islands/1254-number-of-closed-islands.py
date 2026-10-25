class Solution:
    def dfs(self,r,c,row,col,grid):
        grid[r][c]=1
        dir=[(0,1),(0,-1),(1,0),(-1,0)]
        for dx,dy in dir:
            nr=r+dx
            nc=c+dy
            if 0<=nr<row and 0<=nc<col and grid[nr][nc]==0:
                self.dfs(nr,nc,row,col,grid)
    def closedIsland(self, grid: list[list[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        for j in range(col):
            if grid[0][j]==0:
                self.dfs(0,j,row,col,grid)
            if grid[row-1][j]==0:
                self.dfs(row-1,j,row,col,grid)       
        for i in range(row):
            if grid[i][0]==0:
                self.dfs(i,0,row,col,grid)
            if grid[i][col-1]==0:
                self.dfs(i,col-1,row,col,grid)
                  
        count=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==0:
                    self.dfs(i,j,row,col,grid)
                    count+=1
        return count
            