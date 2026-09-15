class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        fs={}
        ft={}
        for i in range(len(s)):
            a=s[i]
            b=t[i]

            if a in fs and fs[a]!=b:
                return False
            if b in ft and ft[b]!=a:
                return False
            fs[a]=b
            ft[b]=a
        return True