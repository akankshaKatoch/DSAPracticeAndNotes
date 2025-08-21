from typing import List
import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left = 0
        right = len(costs) - 1

        minheapleft = []
        minheapright = []

        tcost = 0

        for i in range(candidates):
            if left<= right:
                heapq.heappush(minheapleft, (costs[left], left) )
                left +=1
            if left<= right:
                heapq.heappush(minheapright, (costs[right], right) )
                right -=1
        print("minheapleft: ", minheapleft[0][0])
        print("minheapright: ", minheapright)
        for i in range(k):
            if minheapright and (not minheapleft or minheapleft[0][0] > minheapright[0][0]):
                cost, idx = heapq.heappop(minheapright)
                tcost += cost
                if left<=right:
                    heapq.heappush(minheapright, (costs[right], right))
                    right -= 1
            else:
                cost, idx = heapq.heappop(minheapleft)
                tcost += cost
                if left<=right:
                    heapq.heappush(minheapleft, (costs[left], left))
                    left += 1
        return tcost


sol = Solution()
costs = [17,12,10,2,7,2,11,20,8]
k = 3
candidates = 4
print(sol.totalCost(costs, k, candidates))

costs = [1, 100, 100, 1]
k = 2
candidates = 1
print(sol.totalCost(costs, k, candidates))

costs = [17, 12, 10, 2, 7, 22, 1]
k = 3
candidates = 2
print(sol.totalCost(costs, k, candidates))