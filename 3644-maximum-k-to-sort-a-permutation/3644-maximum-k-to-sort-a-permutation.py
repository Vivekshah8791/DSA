class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        sorted_nums=sorted(nums)
        if nums==sorted_nums:
            return 0
        arr=[]
        for i in range(len(nums)):
            if nums[i]!=i:
                arr.append(nums[i])
        ans=arr[0]
        for i in range(1,len(arr)):
            ans=ans&arr[i]
        return ans