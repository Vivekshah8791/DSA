class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increase=1
        decrease=1
        l1=1
        l2=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                l1+=1
                increase=max(increase,l1)
            else:
                l1=1
            if nums[i]<nums[i-1]:
                l2+=1
                decrease=max(decrease,l2)
            else:
                l2=1
        return max(increase,decrease)
