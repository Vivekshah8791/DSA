class Solution:
    def solve(self,r,c,row,col,dp,grid):
        if r>=row or c>=col:
            return float("inf")
        if r==row-1 and c==col-1:
            return grid[r][c]
        if dp[r][c]!=-1:
            return dp[r][c]
        right=self.solve(r,c+1,row,col,dp,grid)
        down=self.solve(r+1,c,row,col,dp,grid)
        dp[r][c]=grid[r][c]+min(right,down)
        return dp[r][c]
    def minPathSum(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        dp=[[-1 for _ in range(col)]for _ in range(row)]
        return self.solve(0,0,row,col,dp,grid)