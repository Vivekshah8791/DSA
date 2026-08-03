import math

class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        ans = -1
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                g = math.gcd(nums[i], nums[j])
                cal = (nums[i] * nums[j]) // (g * g)
                if cal > ans:
                    ans = cal
                    
        return ans