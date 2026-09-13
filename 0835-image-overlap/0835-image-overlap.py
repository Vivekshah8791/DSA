class Solution:

    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        matching = set()
        n = len(img1)
        for i in range(n):
            for j in range(n):
                if img2[i][j] == 1:
                    matching.add((i, j))
        ones = []
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    ones.append((i, j))
        maxi = 0
        for dx in range(-(n - 1), n):
            for dy in range(-(n - 1), n):
                count = 0
                for x, y in ones:
                    nx = x + dx
                    ny = y + dy
                    if (nx, ny) in matching:
                        count += 1
                maxi = max(maxi, count)
        return maxi