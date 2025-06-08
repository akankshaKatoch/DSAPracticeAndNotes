"""
Problem Statement. Meeting Rooms

Given an array of meeting time intervals where intervals[i] = [starti, endi], 
determine if a person could attend all meetings.
Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Example 2:
Input: intervals = [[7,10],[2,4]]
Output: true

Constraints:
0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti < endi <= 106
 
"""
from typing import List
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        #sort by the start time
        intervals.sort(key = lambda x: x[0])
        print(intervals)
        for i in range(1, len(intervals)):
            #previous interval end time should be less than start time of current interval
            prev = intervals[i-1]
            curr = intervals[i]

            if prev[1]>curr[0]:
                return False
            """
            Shorter version:
            if intervals[i-1][1] > intervals[i][0]:
                return False
            """
        return True


intervals = [[0,30],[5,10],[15,20]]
sol = Solution()
print(sol.canAttendMeetings(intervals))
intervals = [[7,10],[2,4]]
print(sol.canAttendMeetings(intervals))
