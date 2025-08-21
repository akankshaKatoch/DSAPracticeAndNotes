from typing import List
import heapq
from collections import defaultdict

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        avg = []

        items.sort(key=lambda x:(x[0],-x[1]))
        #print(items)

        i = 0
        n = len(items)

        while i<n:
            sid = items[i][0]
            total = 0
            cnt = 0

            while i< n and items[i][0]== sid and cnt < 5:
                total += items[i][1]
                cnt += 1
                i+=1
            while i<n and  items[i][0] == sid:
                i+= 1
            avg.append([sid, total//5])
        

        return avg
    
    def highFiveheap(self, items: List[List[int]]) -> List[List[int]]:

        #pq helps in sorting as well. 
        heaps = defaultdict(list)

        for sid, score in items:
            heap = heaps[sid]
            heapq.heappush(heap, score)
            #print(heap)
            if len(heap)>5:
                heapq.heappop(heap)
        #print(heaps)

        res = []
        for sid in sorted(heaps.keys()):
            res.append([sid, sum(heaps[sid])//5])

        return res

sol= Solution()
items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
print(sol.highFive(items))
print(sol.highFiveheap(items))