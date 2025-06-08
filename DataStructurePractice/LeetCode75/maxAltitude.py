from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxaltitude = 0
        current = 0

        for i in gain:
            current = current + i
            maxaltitude = max(current, maxaltitude)

            print(current, ", ",maxaltitude)
        print(i) 
        return maxaltitude

gain = [-5,1,5,0,-7]
gain = [-4,-3,-2,-1,4,3,2]
sol = Solution()
print(sol.largestAltitude(gain))