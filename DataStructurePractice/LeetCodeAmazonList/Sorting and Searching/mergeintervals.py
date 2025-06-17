from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])
        #print(intervals)
        mergedList = [intervals[0]]

        for currList in intervals[1:]:
            #print(curr) #this is peeking 
            temp = mergedList[-1]

            if temp[1] >= currList[0]:
                temp[1] = max(temp[1], currList[1]) 
            else: 
                mergedList.append(currList)
            #print(temp)
        #print(mergedList)
        return mergedList

intervals = [[1,4],[2,3]]
sol = Solution()
print(sol.merge(intervals))