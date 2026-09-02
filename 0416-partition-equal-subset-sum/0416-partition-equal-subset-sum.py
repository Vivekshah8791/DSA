class Solution:
    def solve(self,index,curr,nums,find,dp):
        if curr==find:
            return True
        if curr>find or index>=len(nums):
            return False
        if dp[index][curr]!=-1:
            return dp[index][curr]
        pick=self.solve(index+1,curr+nums[index],nums,find,dp)
        notpick=self.solve(index+1,curr,nums,find,dp)
        dp[index][curr]=pick or notpick
        return dp[index][curr]
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total%2!=0:
            return False
        find=total//2
        dp=[[-1 for _ in range(find+1)]for _ in range(len(nums))]
        return self.solve(0,0,nums,find,dp)