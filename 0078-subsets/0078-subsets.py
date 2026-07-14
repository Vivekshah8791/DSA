class Solution:
    def solve(self,nums,index,sub,ans):
        if index==len(nums):
            ans.append(sub[:]) 
            return       
        sub.append(nums[index])
        self.solve(nums,index+1,sub,ans)
        sub.pop()
        self.solve(nums,index+1,sub,ans)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        sub=[]
        self.solve(nums,0,sub,ans)
        return ans