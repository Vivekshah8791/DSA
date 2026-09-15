class Solution:
    def reverseWords(self, s: str) -> str:
        news=list(s.strip().split())
        return " ".join(news[::-1])