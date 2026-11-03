class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for q in queries:
            l,r,k,v=q
            index=l
            while index<=r:
                nums[index]=(nums[index]*v)%(10**9+7)
                index+=k
        ans=0
        for n in nums:
            ans^=n
        return ans