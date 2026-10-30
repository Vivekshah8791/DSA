class Solution:
    def findSmallestInteger(self, nums: list[int], value: int) -> int:
        freq = {}
        for num in nums:
            x = num % value
            if x not in freq:
                freq[x] = 1
            else:
                freq[x] += 1
        ans = 0
        while freq.get(ans % value, 0) > 0:
            freq[ans % value] -= 1
            ans += 1
        return ans