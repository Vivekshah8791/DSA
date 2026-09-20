class Solution:
    def shortestPalindrome(self, s: str) -> str:
        original=s
        s=s+"#"+s[::-1]
        n=len(s)
        lps=[0]*n
        i=1
        le=0
        while i<n:
            if s[i]==s[le]:
                le+=1
                lps[i]=le
                i+=1
            else:
                if le!=0:
                    le=lps[le-1]
                else:
                    i+=1
        longest=lps[-1]
        return original[longest::][::-1]+original