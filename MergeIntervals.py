import numpy as np
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==1: return intervals
        pop_idx=[]
        intervals.sort()
        print(intervals)
        idx=1
        while(idx<len(intervals)):
            if intervals[idx-1][1]>=intervals[idx][0]:
                st=intervals[idx-1][0] if intervals[idx-1][0]<intervals[idx][0] else intervals[idx][0]
                end=intervals[idx][1] if intervals[idx][1]>intervals[idx-1][1] else intervals[idx-1][1]
                intervals[idx-1]=[st,end]
                intervals.pop(idx)
            else:
                idx+=1
       
        return intervals