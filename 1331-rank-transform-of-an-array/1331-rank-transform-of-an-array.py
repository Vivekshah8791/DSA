class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        cop=sorted(arr)
        dic={}
        start=1
        for i in range(len(cop)):
            if cop[i] not in dic:
                dic[cop[i]]=start
                start+=1
        ans=[]
        for j in range(len(arr)):
            ans.append(dic[arr[j]])
        return ans
            
