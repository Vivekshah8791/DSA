class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i,n in enumerate(nums):
            sumi=0
            while n>0:
                sumi+=n%10
                n//=10
            if sumi==i:
                return i
        return -1
