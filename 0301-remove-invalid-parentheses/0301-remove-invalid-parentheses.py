class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        ans=set()
        left=0
        right=0
        for ch in s:
            if ch=="(":
                left+=1
            elif ch==")":
                if left>0:
                    left-=1
                else:
                    right+=1
        def solve(index,valid,balance,left,right):
            if balance<0:
                return 
            if index==len(s):
                if balance==0 and left==0 and right==0:
                    ans.add(valid)
                    return 
                return 
            ch=s[index]
            if ch.isalpha():
                solve(index+1,valid+ch,balance,left,right)
            elif ch=="(":
                solve(index+1,valid+ch,balance+1,left,right)
                if left>0:
                    solve(index+1,valid,balance,left-1,right)
            else:
                solve(index+1,valid+ch,balance-1,left,right)
                if right>0:
                    solve(index+1,valid,balance,left,right-1)
        solve(0,"",0,left,right)
        return list(ans)
                    



                