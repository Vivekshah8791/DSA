class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        le=len(nums)//3
        freq={}
        ans=[]
        for n in nums:
            freq[n]=freq.get(n,0)+1
            if freq[n]==le+1:
                ans.append(n)
        return ans
