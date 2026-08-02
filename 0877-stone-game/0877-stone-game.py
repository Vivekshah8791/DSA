class Solution:
    def solve(self,piles,left,right,dp):
        if left>right:
            return 0
        if left==right:
            return piles[left]
        if (left,right) in dp:
            return dp[(left,right)]
        takeleft=piles[left]-self.solve(piles,left+1,right,dp)
        takeright=piles[right]-self.solve(piles,left,right-1,dp)
        dp[(left,right)]=max(takeleft,takeright)
        return dp[(left,right)]
    def stoneGame(self, piles: List[int]) -> bool:
        dp={}
        return self.solve(piles,0,len(piles)-1,dp)>0