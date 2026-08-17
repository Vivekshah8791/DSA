class Solution:
    def solve(self,maxSum,nums,k):
        subarray=1
        curr=0
        for n in nums:
            if curr+n<=maxSum:
                curr+=n
            else:
                subarray+=1
                curr=n
        return subarray<=k
    def splitArray(self, nums: List[int], k: int) -> int:
        left=max(nums)
        right=sum(nums)
        ans=0
        while left<=right:
            mid=left+(right-left)//2
            if self.solve(mid,nums,k):
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans
