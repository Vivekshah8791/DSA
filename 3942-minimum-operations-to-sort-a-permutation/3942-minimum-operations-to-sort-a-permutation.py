class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return -1
        target=list(range(n))
        k= nums.index(0)
        ans=float("inf")
        if nums[k:]+nums[:k]==target:
            ans=min(ans,k)
            ans=min(ans,n-k+2)
        rev_nums=nums[::-1]
        rev_k=rev_nums.index(0)
        if rev_nums[rev_k:]+rev_nums[:rev_k]==target:
            ans=min(ans,rev_k+1,n-rev_k+1)
        return ans if ans!=float("inf") else -1
