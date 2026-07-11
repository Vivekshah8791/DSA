class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i=0
        one=0
        two=n-1
        while i<=two:
            if nums[i]==0:
                nums[i],nums[one]=nums[one],nums[i]
                one+=1
            elif nums[i]==2:
                nums[i],nums[two]=nums[two],nums[i]
                two-=1
                i-=1
            i+=1

            
        

