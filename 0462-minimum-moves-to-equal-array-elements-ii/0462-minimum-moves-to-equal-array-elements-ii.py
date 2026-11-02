class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n=len(nums)
        nums.sort()
        mid=0
        if len(nums)%2!=0:
            mid=nums[n//2]
        else:
            first=nums[n//2]
            second=nums[(n+1)//2]
            mid=(first+second)//2
        print(mid)
        diff=0
        for n in nums:
            diff+=abs(n-mid)
        return diff