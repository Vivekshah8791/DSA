class Solution:
    def solve(self,num):
        if num<=9:
            return num
        copy=num
        sumi=0
        while copy>0:
            sumi+=copy%10
            copy//=10
        return self.solve(sumi)
    def addDigits(self, num: int) -> int:
        return self.solve(num)