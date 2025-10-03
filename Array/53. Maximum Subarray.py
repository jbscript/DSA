# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Example 2:
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


# def maxSubArray(nums: list[int]) -> int:
#     max_sum_so_far = nums[0]

#     for i in range(len(nums)):
#         current_max = 0
#         for j in range(i, len(nums)):
#             current_max += nums[j]
#             max_sum_so_far = max(max_sum_so_far, current_max)
#     return max_sum_so_far


def maxSubArrayOptimal(nums: list[int]) -> int:
    current_sum = 0
    max_sum = nums[0]

    for i in range(len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    return max_sum


response = maxSubArrayOptimal([5, 4, -1, 7, 8])
print(response)
