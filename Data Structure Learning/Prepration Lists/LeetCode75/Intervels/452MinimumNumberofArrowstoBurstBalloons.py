from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points.sort(key=lambda x:x[1])
        count = 1
        end = points[0][1]

        for s, e in points[1:]:
            
            if s>end:
                count += 1
                end = e
        return count        
        