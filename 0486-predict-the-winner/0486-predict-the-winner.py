class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        dp={}
        def solve(nums,left,right,dp):
            if left>right:
                return 0
            if left==right:
                return nums[left]
            if (left,right) in dp:
                return dp[(left,right)]
            takeleft=nums[left]-solve(nums,left+1,right,dp)
            takeright=nums[right]-solve(nums,left,right-1,dp)
            dp[(left,right)]=max(takeleft,takeright)
            return dp[(left,right)]
        return solve(nums,0,len(nums)-1,dp)>=0