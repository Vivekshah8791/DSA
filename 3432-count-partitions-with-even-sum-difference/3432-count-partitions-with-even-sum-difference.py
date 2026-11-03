class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total=sum(nums)
        running=0
        count=0
        for i in range(len(nums)-1):
            running+=nums[i]
            right=total-running
            if abs(right-running)%2==0:
                count+=1
        return count