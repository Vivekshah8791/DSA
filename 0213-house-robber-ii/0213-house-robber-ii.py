class Solution:
    def solve(self,nums,index,n,dp):
        if index>=n:
            return 0
        if dp[index]!=-1:
            return dp[index]
        pick=nums[index]+self.solve(nums,index+2,n,dp)
        not_pick=self.solve(nums,index+1,n,dp)
        dp[index]=max(pick,not_pick)
        return dp[index]
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        dp1=[-1]*n
        case1=self.solve(nums,0,n-1,dp1)
        dp2=[-1]*n
        case2=self.solve(nums,1,n,dp2)
        return max(case1,case2)
