class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        count=0
        for n in nums:
            if n==0:
                count+=1
        if count==len(nums):
            return 0
        
        xor=0
        for n in nums:
            xor^=n
        if xor !=0:
            return len(nums)
        else:
            return len(nums)-1
            