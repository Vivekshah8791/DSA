class Solution:
    def solve(self,r,c,nc,row,col,dp,grid):
        if r>=row or c<0 or c>=col or nc<0 or nc>=col:
            return float("-inf")
        if r==row-1:
            if c==nc:
                return grid[r][c]
            return grid[r][c]+grid[r][nc]
        if dp[r][c][nc]!=-1:
            return dp[r][c][nc]
        if c==nc:
            current=grid[r][c]
        else:
            current=grid[r][c]+grid[r][nc]
        ans=float("-inf")
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                ans=max(ans,self.solve(r+1,c+i,nc+j,row,col,dp,grid))
        dp[r][c][nc]=current+ans
        return dp[r][c][nc]

    def cherryPickup(self,grid:List[List[int]])->int:
        row=len(grid)
        col=len(grid[0])
        dp=[[[-1 for _ in range(col)]for _ in range(col)]for _ in range(row)]
        return self.solve(0,0,col-1,row,col,dp,grid)