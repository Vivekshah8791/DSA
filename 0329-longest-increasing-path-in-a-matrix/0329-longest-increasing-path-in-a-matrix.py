class Solution:
    def longestIncreasingPath(self, grid: list[list[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dir = [(0,1), (0,-1), (1,0), (-1,0)]
        dp = [[0 for _ in range(col)] for _ in range(row)]
        def dfs(r, c):
            if dp[r][c]:
                return dp[r][c]
            path = 1
            for dx, dy in dir:
                nr = r + dx
                nc = c + dy
                if (0 <= nr < row and 0 <= nc < col
                    and grid[nr][nc] > grid[r][c]):
                    path = max(path, 1 + dfs(nr, nc))
            dp[r][c] = path
            return path
        ans = 0
        for i in range(row):
            for j in range(col):
                ans = max(ans, dfs(i, j))
        return ans