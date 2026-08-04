class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        maxi=max(nums)
        mini=min(nums)
        num_set=set(nums)
        ans=[]
        for i in range(mini,maxi+1):
            if i not in num_set:
                ans.append(i)
        return ans