class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals, key = lambda x: x[0])
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
                
        return ans