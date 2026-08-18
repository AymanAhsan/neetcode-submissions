class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        res = [sorted_intervals[0]]
        for i in range(1, len(sorted_intervals)):
            curr = res[-1]
            if curr[1] >= sorted_intervals[i][0]:
                res[-1] = [min(curr[0], sorted_intervals[i][0]), max(curr[1], sorted_intervals[i][1])]
            else:
                res.append(sorted_intervals[i])
        
        return res