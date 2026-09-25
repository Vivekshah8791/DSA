class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n=len(s)
        match=[False]*(n+1)
        match[0]=True
        for i in range(n):
            if match[i]:
                for word in wordDict:
                    if s[i:i+len(word)]==word:
                        match[i+len(word)]=True
        return match[n]