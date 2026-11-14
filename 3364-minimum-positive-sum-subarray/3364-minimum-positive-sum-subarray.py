class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans=float("inf")
        for left in range(len(nums)):
            for right in range(left,min(len(nums),left+r)):
                diff=right-left+1
                if l<=diff<=r:
                    total=sum(nums[left:right+1])
                    if total>0:
                        ans=min(ans,total)
        return ans if ans!=float("inf") else -1

            

