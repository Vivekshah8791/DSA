class Solution:
    def solve(self,index,match,s,t,dp):
        if match==len(t):
            return 1
        if index>=len(s):
            return 0
        if dp[index][match]!=-1:
            return dp[index][match]
        pick=0
        if s[index]==t[match]:
            pick=self.solve(index+1,match+1,s,t,dp)
        notpick=self.solve(index+1,match,s,t,dp)
        dp[index][match]=pick+notpick
        return dp[index][match]
    def numDistinct(self, s: str, t: str) -> int:
        dp=[[-1 for _ in range(len(t))]for _ in range(len(s))]
        return self.solve(0,0,s,t,dp)