class Solution:
    def solve(self,index1,index2,text1,text2,dp):
        if index1==len(text1) or index2==len(text2):
            return 0
        if dp[index1][index2]!=-1:
            return dp[index1][index2]
        if text1[index1]==text2[index2]:
            dp[index1][index2]=1+self.solve(index1+1,index2+1,text1,text2,dp)
        else:
            dp[index1][index2]=max(self.solve(index1+1,index2,text1,text2,dp),self.solve(index1,index2+1,text1,text2,dp))
        return dp[index1][index2]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        dp=[[-1 for _ in range(m)]for _ in range(n)]
        return self.solve(0,0,text1,text2,dp)