class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        sum_arr=[]
        for i,n in enumerate(nums):
            sumi=0
            ori=n
            while n>0:
                sumi+=n%10
                n//=10
            sum_arr.append([i,sumi,ori])
        sum_arr.sort(key=lambda x: (x[1],x[2]))
        swaps=0
        visited=[False]*(len(nums))
        for i in range(len(nums)):
            if visited[i] or sum_arr[i][0]==i:
                continue
            j=i
            cycle=0
            while not visited[j]:
                visited[j]=True
                j=sum_arr[j][0]
                cycle+=1
            swaps+=cycle-1
        return swaps

