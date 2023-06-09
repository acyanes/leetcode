class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for index, [start, end] in enumerate(intervals, start=1):
            lastStart, lastEnd = res[-1]
            if start <= lastEnd:
                res[-1][1]=max(lastEnd, end)
            else:
                res.append([start,end])   
        return res
        

