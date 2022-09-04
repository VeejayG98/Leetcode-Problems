class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals, key = lambda x: x[0])
        prev = [0, 0]
        
        for i in range(len(intervals)):
            start, end = intervals[i]
            if start < prev[1]:
                return False
            else:
                prev = [start, end]
        
        return True