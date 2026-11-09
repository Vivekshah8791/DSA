class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        rows = [0] * row
        cols = [0] * col
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
        ans = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    if rows[i] > 1 or cols[j] > 1:
                        ans += 1
        return ans