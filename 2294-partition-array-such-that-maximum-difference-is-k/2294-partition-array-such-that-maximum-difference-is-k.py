class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        count=0
        mini=float("inf")
        maxi=float("-inf")
        right=0
        n=len(nums)
        while right<n:
            mini=min(mini,nums[right])
            maxi=max(maxi,nums[right])
            if maxi-mini<=k:
                right+=1
            else:
                count+=1
                mini=float("inf")
                maxi=float("-inf")
        return count+1
