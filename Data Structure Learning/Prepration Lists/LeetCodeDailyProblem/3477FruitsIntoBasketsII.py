from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        used = [False]*len(baskets)
        unplaces = 0
        for size in fruits:
            placed = False

            for j in range(len(baskets)):
                print("hello valstored", j)
                if size <= baskets[j] and not used[j]:
                    used[j] = True
                    placed = True
                    break
            if not placed:
                print("j", j, )
                unplaces += 1
        return unplaces

        



sol = Solution()
fruits = [3,6,1]
baskets = [6,4,7]

print(sol.numOfUnplacedFruits(fruits, baskets))