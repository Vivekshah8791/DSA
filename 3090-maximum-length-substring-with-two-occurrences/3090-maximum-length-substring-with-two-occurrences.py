class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l=0
        ans=float("-inf")
        freq={}
        for r in range(len(s)):
            if s[r] not in freq:
                freq[s[r]]=1
            else:
                freq[s[r]]+=1
            while freq[s[r]]>2:
                freq[s[l]]-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans