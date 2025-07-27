from typing import List
from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            #print(i)
            for j in range(i+1, len(nums)):
                #print(i, j)
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []
    
    def twosumusingDic(self, nums: List[int], target: int) -> List[int]:
        dict = defaultdict()

        for i in range(len(nums)):
            if nums[i] in dict:
                return [dict[nums[i]], i]
            
            dict[target - nums[i]] = i
        return []

nums = [3,2,4]
target = 6
sol = Solution()
print(sol.twoSum(nums, target))
print(sol.twosumusingDic(nums, target))



        