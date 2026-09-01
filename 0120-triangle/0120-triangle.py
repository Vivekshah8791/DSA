class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row = len(triangle)
        dp = [[-1 for _ in range(row)] for _ in range(row)]
        for i in range(row):
            dp[row-1][i]=triangle[row-1][i]
        for r in range(row-1, -1, -1):
            for c in range(len(triangle[r])-1, -1, -1):
                if r == row-1:
                    continue
                down = float("inf")
                dia = float("inf")
                if r+1 < row:
                    down = dp[r+1][c]
                if r+1 < row and c+1 < len(triangle[r+1]):
                    dia = dp[r+1][c+1]
                dp[r][c] = triangle[r][c] + min(down, dia)
        return dp[0][0]