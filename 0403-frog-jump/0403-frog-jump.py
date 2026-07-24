class Solution:
    def solve(self, index, last, stones, dp, indexMap):
        if index == len(stones) - 1:
            return True
        if dp[index][last] != -1:
            return dp[index][last]
        ans = False
        for k in (-1, 0, 1):
            jump = last + k
            if jump <= 0:
                continue
            nextPos = stones[index] + jump
            if nextPos not in indexMap:
                continue
            if self.solve(indexMap[nextPos], jump, stones, dp, indexMap):
                ans = True
                break
        dp[index][last] = ans
        return ans
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        n = len(stones)
        indexMap = {stone: i for i, stone in enumerate(stones)}
        dp = [[-1] * (n + 1) for _ in range(n)]
        return self.solve(1, 1, stones, dp, indexMap)