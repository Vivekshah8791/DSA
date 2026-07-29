class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x :x[0])
        merge=[]
        merge.append(intervals[0])
        for i in range(1,len(intervals)):
            item=intervals[i]
            if item[0]<=merge[-1][1]:
                merge[-1]=[min(merge[-1][0],item[0]),max(item[1],merge[-1][1])]
            else:
                merge.append(item)
        return merge