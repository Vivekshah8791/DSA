class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count=0
        ans=0
        for ch in s:
            if ch=="(":
                count+=1
            elif ch==")" and count>0:
                count-=1
            else:
                ans+=1
        return count+ans