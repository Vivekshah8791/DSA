class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        intervals.append([newInterval[0],newInterval[1]])
        intervals.sort()
        print(intervals)
        arr=[]
        arr.append(intervals[0])
        done=0
        for i in range(1,len(intervals)):
            start=arr[-1][0]
            end=arr[-1][1]
            newstart=intervals[i][0]
            newend=intervals[i][1]
            if newstart<=end:
                arr[-1]=[min(start,newstart),max(end,newend)]
            else:
                arr.append([newstart,newend])
        return arr