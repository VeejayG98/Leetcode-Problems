class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x: [x[0], x[1] - x[0]])
        prev = intervals[0]
        count = 0
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] >= prev[1]:
                prev = interval
            elif interval[1] < prev[1]:
                prev = interval
                count += 1
            else:
                count += 1
        
        return count