class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m,n=len(grid),len(grid[0])
        dp=[[set()  for _ in range(n)] for _ in range(m)]
        dp[0][0].add(grid[0][0])

        for r in range(m):
            for c in range(n):
                if not dp[r][c]:
                    continue
                for current_xor in dp[r][c]:
                    if c+1<n:
                        dp[r][c+1].add(current_xor^grid[r][c+1])
                    if r+1<m:
                        dp[r+1][c].add(current_xor^grid[r+1][c])
        return min(dp[m-1][n-1])
                        