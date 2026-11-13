class Solution:
    def minSwapsCouples(self, row: list[int]) -> int:
        pair={}
        i=0
        while i<len(row):
            pair[i]=i+1
            pair[i+1]=i
            i+=2
        ans=0
        i=0
        while i<len(row):
            first=row[i]
            second=pair[row[i]]
            if second!=row[i+1]:
                ans+=1
                for j in range(len(row)):
                    if row[j]==second:
                        row[i+1],row[j]=row[j],row[i+1]
                        break
            i+=2
        return ans

