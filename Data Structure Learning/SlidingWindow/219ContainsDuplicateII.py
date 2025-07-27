from typing import List

def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

    left = 0
    #right = left+1
    # we dont want to use two loops n square complexity. 
    '''
    for left in range(len(nums) - k):
        right= left+1
        while right<= left+k:
            if nums[right] == nums[left] and abs(left-right)<=k:
                return True
            right +=1

    return False
    '''
    window = set()
    for i, num in enumerate(nums):
        if num in window:
            return True
        window.add(num)
        if len(window)> k:
            window.remove(nums[i-k])
    return False
        



s = [99, 99]
k = 2
print(containsNearbyDuplicate(s, k)) 