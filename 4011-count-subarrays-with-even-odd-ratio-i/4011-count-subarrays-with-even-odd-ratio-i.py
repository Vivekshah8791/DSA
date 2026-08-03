class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            even_count = 0
            odd_count = 0
            for j in range(i, n):
                if nums[j] % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1
                if odd_count > 0 and (even_count * b <= odd_count * a):
                    ans += 1

        return ans