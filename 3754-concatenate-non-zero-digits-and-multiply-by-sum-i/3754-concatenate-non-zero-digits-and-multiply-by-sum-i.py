class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x=0
        sumi=0
        one=1
        while n>0:
            rem=n%10
            if rem!=0:
                x=rem*one+x
                one*=10
                sumi+=rem
            n=n//10
        return x*sumi
            
        