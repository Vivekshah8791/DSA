class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                l=len(set(nums[i:j]))
                ans+=l**2
        return ans