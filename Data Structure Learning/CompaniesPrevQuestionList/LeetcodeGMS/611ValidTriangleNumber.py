from typing import List 

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:

        nums.sort()
        count = 0
        n = len(nums)

        
        for k in range(n-1, 1, -1):
            #print("for", k)
            i = 0
            j = k-1
            while i<j:
                #print(nums[i], nums[j], nums[k])
                if nums[i] + nums[j] > nums[k] :
                    count += j- i
                    #print(count)
                    j -= 1
                else:
                    i+= 1
                

        return count
        

sol = Solution()
nums = [2,2,3,4]
print(sol.triangleNumber(nums))
nums = [4,2,3,4]
print(sol.triangleNumber(nums))