def findMaxLength(nums):
    sum_index = {0: -1}  # sum 0 seen at index -1 (helps with edge case)
    running_sum = 0
    max_len = 0

    for i, num in enumerate(nums):
        if num == 0:
            running_sum -= 1
        else:
            running_sum += 1

        if running_sum in sum_index:
            length = i - sum_index[running_sum]
            max_len = max(max_len, length)
        else:
            sum_index[running_sum] = i

    return max_len


Input = [0,1,1,1,1,1,0,0,0]
print(findMaxLength(Input))