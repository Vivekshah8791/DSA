class Solution:
    def assignUmbrella(self, rain: list[int]) -> list[str]:
        freq={"alice":0,"bob":0}
        ans=[]
        for i in range(len(rain)-1):
            if rain[i]==rain[i+1]==1:
                if freq["alice"]==freq["bob"]:
                    ans.append("Alice")
                    freq["alice"]+=1
                elif freq["alice"]>freq["bob"]:
                    ans.append("Bob")
                    freq["bob"]+=1
                else:
                    ans.append("Alice")
                    freq["alice"]+=1
            elif rain[i]==1:
                ans.append("Bob")
                freq["bob"]+=1
            else:
                ans.append("None")
        if rain[len(rain)-1]==0:
            ans.append("None")
        else:
            ans.append("Bob")
        return ans