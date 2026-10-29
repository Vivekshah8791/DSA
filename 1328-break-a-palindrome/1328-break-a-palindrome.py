class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        change=False
        l=list(palindrome)
        n=len(l)
        if n<=1:
            return ""
        for i in range(n//2):
            if l[i]!='a':
                change=True
                l[i]="a"
                break
        if change:
            return "".join(l)
        else:
            l[n-1]="b"
            return "".join(l)
