class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        n = len(arr)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]   
        ans = 0
        for left in range(n):
            for right in range(left, n):
                length = right - left + 1
                if length % 2 != 0:
                    ans += prefix[right + 1] - prefix[left]
        return ans