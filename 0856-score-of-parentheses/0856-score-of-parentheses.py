class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        def solve(left, right):
            if right - left == 2:
                return 1
            count = 0
            for i in range(left, right):
                if s[i] == "(":
                    count += 1
                else:
                    count -= 1
                if count == 0:
                    if i == right - 1:
                        return 2 * solve(left + 1, right - 1)
                    return solve(left, i + 1) + solve(i + 1, right)
        return solve(0, len(s))