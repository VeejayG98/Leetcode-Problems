class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        n = len(intervals)
        idx = 0
        newStart = newInterval[0]
        newEnd = newInterval[1]
        ans = []
        while idx < n and intervals[idx][0] < newStart:
            ans.append(intervals[idx])
            idx += 1
        
        if ans and ans[-1][1] >= newStart:
            ans[-1][1] = max(ans[-1][1], newEnd)
        else:
            ans.append(newInterval)
        
        while idx < n:
            interval = intervals[idx]
            if interval[0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], interval[1])
            else:
                ans.append(interval)
            idx += 1
        return ans