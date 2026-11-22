class Solution:
    def checkString(self, s: str) -> bool:
        a=-1
        b=-1
        for i in range(len(s)):
            if b==-1 and s[i]=='b':
                b=i
            if s[i]=='a':
                a=i
        if a<b or a==-1 or b==-1:
            return True
        return False
