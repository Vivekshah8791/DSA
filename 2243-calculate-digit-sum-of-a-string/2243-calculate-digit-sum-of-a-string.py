
class Solution:
    def solve(self, s, k):
        if len(s) <= k:
            return s
        news = ""
        for i in range(0, len(s), k):
            group = s[i:i+k]
            total = 0
            for digit in group:
                total += int(digit)
            news += str(total)
        return self.solve(news, k)
    def digitSum(self, s: str, k: int) -> str:
        return self.solve(s, k)
