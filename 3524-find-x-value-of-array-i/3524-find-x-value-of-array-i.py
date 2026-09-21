class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dp = [[0] * k for _ in range(n)]
        ans = [0] * k
        r = nums[0] % k
        dp[0][r] = 1
        ans[r] += 1
        for i in range(1, n):
            r = nums[i] % k
            dp[i][r] += 1
            for old_r in range(k):
                if dp[i - 1][old_r] > 0:
                    new_r = (old_r * nums[i]) % k
                    dp[i][new_r] += dp[i - 1][old_r]
            for r in range(k):
                ans[r] += dp[i][r]
        return ans