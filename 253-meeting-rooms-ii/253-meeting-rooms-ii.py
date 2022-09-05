class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x: x[0])
        rooms = []
        for interval in intervals:
            if not rooms or rooms[0] > interval[0]:
                heapq.heappush(rooms, interval[1])
            else:
                heapq.heappop(rooms)
                heapq.heappush(rooms, interval[1])
        return len(rooms)