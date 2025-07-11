def mycode(nums, k):
    maxelemet = max(nums)
    maxGlbal = float('-inf')
    winSum = sum(nums[0:k])
    window = nums[:k]

    mininwin = min(window)
    replacesum = winSum - mininwin + maxelemet
    maxGlbal = max(maxGlbal, winSum, replacesum)
    
    for i in range(k, len(nums)):
        winSum = winSum - nums[i-k] + nums[i]
        window.pop(0)
        window.append(nums[i])

        mininwin = min(window)
        replacesum = winSum - mininwin + maxelemet

        maxGlbal = max(maxGlbal, winSum, replacesum)
               

    return maxGlbal/float(k)




nums = [1, 12, -5, -6, 50, 3] 
k = 3 
print(mycode(nums, k))