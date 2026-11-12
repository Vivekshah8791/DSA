
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [-1 for _ in range(n+1)]
        def solve(index):
            if index == n:
                return 0
            if dp[index] != -1:
                return dp[index]
            first = float('inf')
            second = float('inf')
            third = float('inf')
            if index+1 <= n:
                first = costs[index] + 1**2 + solve(index+1)
            if index+2 <= n:
                second = costs[index+1] + 2**2 + solve(index+2)
            if index+3 <= n:
                third = costs[index+2] + 3**2 + solve(index+3)
            dp[index] = min(first, second, third)
            return dp[index]
        return solve(0)
