import math
class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n=len(nums)
        divisors=[n]
        divisors = []
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        ans=0
        for k in divisors:
            check=[]
            i=0
            while i<n:
                arr=nums[i:i+k]
                part=-1
                for j in range(len(arr)-1):
                    if arr[j]>arr[j+1]:
                        part=j
                        break
                if part!=-1:
                    arr=arr[part+1:]+arr[0:part+1]
                check.extend(arr)
                i=i+k
            flag=True
            for l in range(len(check)-1):
                if check[l]>check[l+1]:
                    flag=False
                    break
            if flag:
                ans+=k
        return ans

            
            
