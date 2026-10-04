class Solution:
    def solve(self, s, index, balance, dp):
        if balance < 0:
            return False
        if index == len(s):
            return balance == 0
        if (index, balance) in dp:
            return dp[(index, balance)]
        ch = s[index]
        if ch == "(":
            ans = self.solve(s, index + 1, balance + 1, dp)
        elif ch == ")":
            ans = self.solve(s, index + 1, balance - 1, dp)
        else:  
            if self.solve(s, index + 1, balance + 1, dp):
                ans = True
            elif self.solve(s, index + 1, balance - 1, dp):
                ans = True
            else:
                ans = self.solve(s, index + 1, balance, dp)
        dp[(index, balance)] = ans
        return ans
    def checkValidString(self, s: str) -> bool:
        dp = {}
        return self.solve(s, 0, 0, dp)