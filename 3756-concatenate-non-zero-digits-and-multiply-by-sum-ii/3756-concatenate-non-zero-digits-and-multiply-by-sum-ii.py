from bisect import bisect_left, bisect_right
class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD=10**9+7
        digit=[]
        pos=[]
        for i,ch in enumerate(s):
            if ch.isdigit() and int(ch)>0:
                digit.append(int(ch))
                pos.append(i)
        n=len(digit)
        prefix_sum=[0]*(n+1)
        for i in range(n):
            prefix_sum[i+1]=prefix_sum[i]+digit[i]
        number=[0]*(n+1)
        for j in range(n):
            number[j+1]=(number[j]*10+digit[j])%MOD
        power=[1]*(n+1)
        for k in range(1,n+1):
            power[k]=(power[k-1]*10)%MOD
        ans=[]
        for l,r in queries:
            left = bisect_left(pos, l)
            right = bisect_right(pos, r) - 1
            if left>right:
                ans.append(0)
                continue
            length=right-left+1
            num=(number[right+1]-number[left]*power[length])%MOD
            sumi=prefix_sum[right+1]-prefix_sum[left]
            ans.append((num*sumi)%MOD)
        return ans

