from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key= lambda x:x[0])

        heap = []

        for meeting in intervals:
            starttime, endtime = meeting[0], meeting[1]

            if heap and starttime >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, endtime)

        return len(heap)