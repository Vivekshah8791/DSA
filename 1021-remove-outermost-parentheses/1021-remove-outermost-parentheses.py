class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        i = 0
        para = ""

        while i < len(s):
            prev = i
            count = 0
            while i < len(s):
                if s[i] == '(':
                    count += 1
                else:
                    count -= 1
                i += 1
                if count == 0:
                    break
            para += s[prev + 1:i - 1]
        return para