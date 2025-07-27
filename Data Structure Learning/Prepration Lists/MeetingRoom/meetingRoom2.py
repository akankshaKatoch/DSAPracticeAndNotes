"""   
253. Meeting Rooms II
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of conference rooms required.
Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
"""
from typing import List
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        


import heapq

def minMeetingRooms(intervals):
    if not intervals:
        return 0

    # Step 1: Sort by start time
    intervals.sort(key=lambda x: x[0])

    # Step 2: Min-heap to track end times
    heap = []

    for meeting in intervals:
        start, end = meeting

        # If the earliest ending meeting is done, remove it
        if heap and heap[0] <= start:
            heapq.heappop(heap)

        # Allocate room for current meeting
        heapq.heappush(heap, end)

    return len(heap)


intervals = [[0,30],[5,10],[15,20]]
sol = Solution()
print(sol.minMeetingRooms(intervals))
intervals = [[7,10],[2,4]]
print(sol.minMeetingRooms(intervals))