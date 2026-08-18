class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq={}
        for i in range(len(nums)-k+1):
            arr=nums[i:i+k]
            for n in set(arr):
                if n in freq:
                    freq[n]+=1
                else:
                    freq[n]=1
        maxi=-1
        for key,value in freq.items():
            if value==1:
                maxi=max(maxi,key)
        return maxi
                
