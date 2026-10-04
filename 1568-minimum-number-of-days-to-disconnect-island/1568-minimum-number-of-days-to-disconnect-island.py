class Solution:
    def solve(self, r, c, row, col, grid):

        grid[r][c] = 0

        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dx, dy in dir:
            nr = r + dx
            nc = c + dy

            if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                self.solve(nr, nc, row, col, grid)

    def minDays(self, grid: list[list[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        temp = [r[:] for r in grid]
        count = 0
        for i in range(row):
            for j in range(col):
                if temp[i][j] == 1:
                    self.solve(i, j, row, col, temp)
                    count += 1
        if count != 1:
            return 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    temp = [r[:] for r in grid]
                    count = 0
                    for x in range(row):
                        for y in range(col):
                            if temp[x][y] == 1:
                                self.solve(x, y, row, col, temp)
                                count += 1
                    if count != 1:
                        return 1
                    grid[i][j] = 1
        return 2