class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n=len(nums)
        prefix_min=[0]*n
        prefix_min[0]=nums[0]
        for i in range(1,n):
            prefix_min[i]=min(prefix_min[i-1],nums[i])
        suffix_min=[0]*n
        suffix_min[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            suffix_min[i]=min(suffix_min[i+1],nums[i])
        ans=float("inf")
        for i in range(1,n-1):
            left_min=prefix_min[i-1]
            right_min = suffix_min[i+1]
            if nums[i]>left_min and nums[i]>right_min:
                ans=min(ans,nums[i]+left_min+right_min)
        return ans if ans!=float("inf") else -1
