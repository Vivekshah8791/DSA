class Solution:
    def reverseDegree(self, s: str) -> int:
        ans=0
        for i,ch in enumerate(s):
            ans+=(ord("a")-ord(ch)+26)*(i+1)
        return ans