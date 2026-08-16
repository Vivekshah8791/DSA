class Solution:
    def solve(self,r,c,row,col,dp):
        if r==row-1 or c==col-1:
            return 1
        if dp[r][c]!=-1:
            return dp[r][c]
        right=self.solve(r,c+1,row,col,dp)
        down=self.solve(r+1,c,row,col,dp)
        dp[r][c]=right+down
        return dp[r][c]
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1 for _ in range(n)]for _ in range(m)]
        return self.solve(0,0,m,n,dp)