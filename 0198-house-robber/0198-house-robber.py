class Solution:
    def solve(self,nums,index,n,dp):
        if index>=n:
            return 0
        if dp[index]!=-1:
            return dp[index]
        not_pick=self.solve(nums,index+1,n,dp)
        pick=self.solve(nums,index+2,n,dp)+nums[index]
        dp[index]=max(pick,not_pick)
        return dp[index]
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*n
        return self.solve(nums,0,n,dp)