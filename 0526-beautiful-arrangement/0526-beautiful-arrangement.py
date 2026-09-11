class Solution:
    def solve(self,ele,mask,place,n):
        if mask==((1<<n)-1):
            return 1
        ans=0
        for i in range(n):
            if place[i]%ele!=0 and ele%place[i]!=0:
                continue
            if (mask)&(1<<i)!=0:
                continue
            nmask=mask|(1<<i)
            ans+=self.solve(ele+1,nmask,place,n)
        return ans
    def countArrangement(self, n: int) -> int:
        place=[i+1 for i in range(n)]
        mask=0
        return self.solve(1,mask,place,n)