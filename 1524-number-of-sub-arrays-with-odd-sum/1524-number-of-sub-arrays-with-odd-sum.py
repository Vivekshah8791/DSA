class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        ans=0
        n=len(arr)
        sumi=0
        mod=10**9+7
        even=1
        odd=0
        for num in arr:
            sumi+=num
            if sumi%2==0:
                ans+=odd
                even+=1
            else:
                ans+=even
                odd+=1
        return ans%mod

