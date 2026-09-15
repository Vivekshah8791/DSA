class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs)<=1:
            return strs[0]
        strs.sort()
        n=len(strs)
        first=strs[0]
        last=strs[-1]
        i=0
        while i<len(first) and i<len(last) and first[i]==last[i]:
            i+=1
        return first[:i]