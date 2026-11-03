class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxi=max(nums)
        ans=0
        for n in nums:
            ans+=abs(maxi-n)
        return ans