class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        count=1
        prev=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==prev:
                count+=1
                if count>2:
                    nums[i]=float("inf")
            else:
                prev=nums[i]
                count=1
        nums.sort()
        ans=0
        for n in nums:
            if n!=float("inf"):
                ans+=1
        return ans