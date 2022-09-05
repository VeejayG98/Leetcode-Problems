class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x: x[0])
        rooms = []
        for interval in intervals:
            # if not rooms:
            #     rooms.append(interval)
            # else:
            intervalAdded = False
            for i in range(len(rooms)):
                if rooms[i][1] <= interval[0]:
                    rooms[i] = interval
                    intervalAdded = True
                    break
            if not rooms or intervalAdded == False:
                rooms.append(interval)
        return len(rooms)