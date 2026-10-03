class Solution:
    def solve(self,s,n,open,close,ans):
        if open==n and close==n:
            ans.append(s[:])
            return
        if close>open:
            return 
        if open<n:
            self.solve(s+"(",n,open+1,close,ans)
        if close<n:    
            self.solve(s+")",n,open,close+1,ans)
    def generateParenthesis(self, n: int) -> list[str]:
        ans=[]
        self.solve("",n,0,0,ans)
        return ans