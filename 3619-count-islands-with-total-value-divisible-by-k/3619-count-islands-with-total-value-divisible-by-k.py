class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        row=len(grid)
        col=len(grid[0])
        ans=0

        def dfs(r,c):
            total=grid[r][c]
            grid[r][c]=0
            dir=[(0,1),(0,-1),(1,0),(-1,0)]
            for dx,dy in dir:
                nr=r+dx
                nc=c+dy
                if 0<=nr<row and 0<=nc<col and grid[nr][nc]!=0:
                    total+=dfs(nr,nc)
            return total

        for i in range(row):
            for j in range(col):
                if grid[i][j]!=0:
                    value=dfs(i,j)
                    if value%k==0:
                        ans+=1
        return ans
            
