from typing import List
class Solution:

    # other solution than two pointers which i soved in oher place. 
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)):
            search = target - numbers[i]

            left = i+1
            right = len(numbers)-1

            while left<=right:
                mid = (left+right)//2

                if search == numbers[mid]:
                    return [i+1, mid+1]
                if numbers[mid] < search:
                    left = mid+1
                else:

                    right = mid -1
        return []




numbers = [5, 25, 75]
target = 100
sol = Solution()
print(sol.twoSum(numbers, target))