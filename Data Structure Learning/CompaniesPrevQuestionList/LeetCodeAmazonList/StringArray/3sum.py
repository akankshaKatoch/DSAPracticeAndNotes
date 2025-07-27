from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sum = 0
        result = []
        print(nums)

        for i in range(len(nums)-2):
        #handling the duplicates we have sorted list. so 1t elemt and second element returns the same list. 
            if i > 0 and nums[i] == nums[i-1]:
                continue

            a = nums[i]
            left = i+1
            right = len(nums) - 1

            while left <right:
                ts = nums[i] + nums[left] + nums[right]

                if ts < 0:
                    left += 1
                elif ts > 0:
                    right -=1
                else:
                    print([nums[i] , nums[left], nums[right]])
                    result.append([nums[i] , nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left +=1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1
                    print('hello')
        
        return result
                




nums =  [-1, 0, 1, 2, -1, -4]

sol = Solution()
print(sol.threeSum(nums))
