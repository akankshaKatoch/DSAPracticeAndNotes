from typing import List 

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        daily = [0]*n
        stack = []

        for i, num in enumerate(temperatures):
            print(i , " - ", num)
            while stack and num>temperatures[stack[-1]]:
                j = stack.pop()
                daily[j] = i-j
                print(daily)
            stack.append(i)
            print(stack)

        return daily
        

sol = Solution()
temperatures = [73,74,75,71,69,72,76,73]
#Output:       [1,1,4,2,1,1,0,0]
print(sol.dailyTemperatures(temperatures))
