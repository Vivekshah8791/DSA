class Solution:
    def solve(self,ip,s,index,ans,parts):
        if parts==4:
            if index==len(s):
                ans.append(ip[:-1:])
                return
        if index>=len(s):
            return
        for l in range(1,4):
            part=s[index:index+l]
            if len(part)>1 and part[0]=="0":
                continue
            if int(part)>255:
                continue
            self.solve(
                ip+part+".",
                s,
                index+l,
                ans,
                parts+1
                )
    def restoreIpAddresses(self, s: str) -> list[str]:
        if len(s)>12 or len(s)<4:
            return []
        ans=[]
        self.solve("",s,0,ans,0)
        return ans