class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left=0
        ans=0
        ch={"a":0,"b":0,"c":0}
        for r in range(len(s)):
            ch[s[r]]+=1
            while ch["a"]>0 and ch["b"]>0 and ch["c"]>0:
                ans+=len(s)-r
                ch[s[left]]-=1
                left+=1
        return ans
            