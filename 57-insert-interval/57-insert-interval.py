class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        newStart, newEnd = newInterval
        i = 0
        n = len(intervals)
        ans = []
        
        while i < n and intervals[i][0] < newStart:
            ans.append(intervals[i])
            i += 1
        if not ans or ans[-1][1] < newStart:
            ans.append(newInterval)
        else:
            ans[-1][1] = max(ans[-1][1], newEnd)
        
        while i < n:
            interval = intervals[i]
            if ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(interval[1], ans[-1][1])
            i += 1
        
        return ans