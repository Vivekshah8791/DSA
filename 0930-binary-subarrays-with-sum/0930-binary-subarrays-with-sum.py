class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        def l(k):
            if k<0:
                return 0
            left = 0
            right = 0
            sumi = 0
            count = 0
            while right < len(nums):
                sumi += nums[right]
                while sumi > k:
                    sumi -= nums[left]
                    left += 1
                count += right - left + 1
                right += 1
            return count
        return l(goal) - l(goal - 1)