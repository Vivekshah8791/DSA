class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[-1]
        maxi=0
        for i,ch in enumerate(s):
            if ch=="(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxi=max(maxi,i-stack[-1])
        return maxi