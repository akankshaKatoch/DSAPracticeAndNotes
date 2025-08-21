from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        result = []

        # to start think one no will be 1 and 2nd no can be 2


        def dfs(start, remaining, path):
            if remaining == 0 and len(path)==k:
                result.append(path[:])
                return 
            if remaining<0 or len(path) == k:
                return
            for num in range(start, 10):
                if num>remaining:
                    break
                path.append(num)
                dfs(num+1, remaining-num, path)
                path.pop()   

        dfs(1, n, []) 
        return result 
        

sol = Solution()
k = 3
n = 7
# [[1,2,4]]
print(sol.combinationSum3(k, n))