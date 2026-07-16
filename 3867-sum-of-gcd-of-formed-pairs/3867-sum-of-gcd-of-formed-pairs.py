class Solution:
    def gcd(self,a,b):
        if b==0:
            return a
        return self.gcd(b,a%b)
    def gcdSum(self, nums: list[int]) -> int:
        maximum=nums[0]  
        mx=[]
        for i in range(len(nums)):
            if nums[i]>=maximum:
                maximum=nums[i]
            mx.append(maximum)
        prefixgcd=[]
        for i in range(len(nums)):
            ngcd=self.gcd(nums[i],mx[i])
            prefixgcd.append(ngcd)
        prefixgcd.sort()
        total=0
        left=0
        right=len(prefixgcd)-1
        while left<right:
            n=self.gcd(prefixgcd[left],prefixgcd[right])
            total+=n
            left+=1
            right-=1
        return total
                
    