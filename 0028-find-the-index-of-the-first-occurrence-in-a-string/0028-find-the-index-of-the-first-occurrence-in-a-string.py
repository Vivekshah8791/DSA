class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        if m == 0:
            return 0
        lps = [0] * m
        i = 1
        le = 0
        while i < m:
            if needle[i] == needle[le]:
                le += 1
                lps[i] = le
                i += 1
            else:
                if le != 0:
                    le = lps[le - 1]
                else:
                    i += 1
        i = 0
        j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == m:
                    return i - m
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1