class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans=0
        for left in range(len(nums)):
            pro=1
            for right in range(left,len(nums)):
                pro*=nums[right]
                if pro==math.gcd(*nums[left:right+1])*math.lcm(*nums[left:right+1]):
                    ans=max(ans,right-left+1)
        return ans