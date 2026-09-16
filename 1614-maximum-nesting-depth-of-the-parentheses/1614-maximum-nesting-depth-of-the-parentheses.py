class Solution:
    def maxDepth(self, s: str) -> int:
        maxi=float("-inf")
        count=0
        for ch in s:
            if ch=='(':
                count+=1
            if ch==")":
                count-=1
            maxi=max(maxi,count)
        return maxi