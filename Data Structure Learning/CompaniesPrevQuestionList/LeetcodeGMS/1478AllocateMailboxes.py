from typing import List

class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)
        sections = houses/k
        if k>= n:
            return 0 

        prefix = [0]*(n+1)

        for i in range(n):
            prefix[i+1] = houses[i] + prefix[i]

        



        for 

        
        