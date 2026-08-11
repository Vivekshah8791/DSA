class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix=nums[0]
        nums_set=set(nums)
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                prefix+=nums[i]
            else:
                break
        while prefix in nums_set:
            prefix+=1
        return prefix
                

