class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sumi=0
        pro=1
        n2=n
        while n2>0:
            rem=n2%10
            sumi+=rem
            pro*=rem
            n2//=10
        total=sumi+pro
        return True if n%total==0 else False