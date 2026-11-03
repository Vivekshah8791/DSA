class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        odd=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                odd.append(0)
            else:
                odd.append(1)
        def sub(goal):
            if goal<0:
                return 0
            count=0
            left=0
            right=0
            sumi=0
            while right<len(nums):
                sumi+=odd[right]
                while sumi>goal:
                    sumi-=odd[left]
                    left+=1
                count+=right-left+1
                right+=1
            return count
        return sub(k)-sub(k-1)
        