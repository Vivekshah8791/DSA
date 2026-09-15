class Solution:
    def largestOddNumber(self, num: str) -> str:
        n=len(num)
        if num[-1] in "13579":
            return num
        ans=""
        i=n-1
        while i>=0 and int(num[i])%2==0:
            i-=1
        return num[:i+1]