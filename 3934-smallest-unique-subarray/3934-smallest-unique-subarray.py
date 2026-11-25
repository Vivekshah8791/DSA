class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        ans = len(nums)
        left, right = 1, len(nums)

        MOD1, BASE1 = 10**9 + 7, 100003
        MOD2, BASE2 = 10**9 + 9, 100019

        def solve(size):
            freq = {}
            p1 = pow(BASE1, size - 1, MOD1)
            p2 = pow(BASE2, size - 1, MOD2)
            h1 = h2 = 0

            for i in range(size):
                h1 = (h1 * BASE1 + nums[i]) % MOD1
                h2 = (h2 * BASE2 + nums[i]) % MOD2
                
            freq[(h1, h2)] = 1

            for i in range(size, len(nums)):
                h1 = (h1 - nums[i - size] * p1) % MOD1
                h1= (h1* BASE1 + nums[i]) % MOD1
                h2 = (h2 - nums[i - size] * p2) %MOD2
                h2 = (h2* BASE2 + nums[i]) % MOD2
                state = (h1, h2)
                freq[state] = freq.get(state, 0) + 1

            return any(val == 1 for val in freq.values())

        while left <= right:
            mid = left + (right - left) // 2
            if solve(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans