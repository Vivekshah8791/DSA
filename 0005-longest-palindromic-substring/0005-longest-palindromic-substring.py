class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        ans=""
        for i in range(n):
            prev=i-1
            next=i+1
            while prev>=0 and next<n and s[prev]==s[next]:
                prev-=1
                next+=1
            news=s[prev+1:next]
            if len(ans)<len(news):
                ans=news
            prev=i
            next=i+1
            while prev>=0 and next<n and s[prev]==s[next]:
                prev-=1
                next+=1
            news=s[prev+1:next]
            if len(ans)<len(news):
                ans=news
        return ans