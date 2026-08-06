class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def cal(n):
            pro=1
            while n>0:
                pro=pro*(n%10)
                n//=10
            return pro
        while cal(n)%t!=0:
            n+=1
        return n