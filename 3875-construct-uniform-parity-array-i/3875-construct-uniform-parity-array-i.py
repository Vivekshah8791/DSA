class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        even=0
        odd=0
        for n in nums1:
            if n%2==0:
                even+=1
            else:
                odd+=1
        if even==len(nums1) or odd==len(nums1):
            return True
        if odd>even:
            l=len(nums1)
            diff=odd-l
            if even>=diff:
                return True
            else:
                return False
        else:
            l=len(nums1)
            diff=even-l
            if even>=diff:
                return True
            else:
                return False
            

