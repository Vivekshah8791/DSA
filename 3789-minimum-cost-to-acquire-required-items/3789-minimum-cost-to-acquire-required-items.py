class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        c1=cost1*need1+cost2*need2
        c2=max(need1,need2)*costBoth
        c3=min(need1,need2)*costBoth
        if need2>need1:
            c3+=(need2-need1)*cost2
        else:
            c3+=(need1-need2)*cost1
        return min(c1,c2,c3)

