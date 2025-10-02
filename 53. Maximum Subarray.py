def maxSubArray(nums):
    max_sum = float("-inf")
    for i in range(len(nums)):
        for j in range(len(nums)):
            current_sum = 0
            for k in range(i, j + 1):
                current_sum += nums[k]
            max_sum = max(current_sum, max_sum)
    return max_sum


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
