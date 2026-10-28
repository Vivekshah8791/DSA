class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        left = 0
        sumi = 0
        ans = n + 1
        for right in range(n):
            sumi += nums[right]
            while sumi >= target:
                ans = min(ans, right - left + 1)
                sumi -= nums[left]
                left += 1
        return 0 if ans == n + 1 else ans