from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x:x[1])
        count = 1
        end = intervals[0][1]
        print(end)

        print(intervals)

        for s, e in intervals[1:]:
            print(s , e)
            if s>=end:
                print("in loop")
                count += 1
                end = e

        return len(intervals)-count




sol = Solution()
intervals = [[1,2],[2,3],[3,4],[1,3]]
print(sol.eraseOverlapIntervals(intervals))