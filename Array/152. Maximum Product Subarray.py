# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

# Example 3:
# Input: nums = nums = [0, 2, 3, -2, 4]
# Output: 6


# def maxProduct(nums: list[int]) -> int:
#     max_product = nums[0]
#     for i in range(len(nums)):
#         current_product = 1
#         for j in range(i, len(nums)):
#             current_product *= nums[j]
#             max_product = max(current_product, max_product)
#     return max_product


def maxProductOptimal(nums: list[int]) -> int:
    max_product = nums[0]
    prefix = 1
    suffix = 1
    for i in range(len(nums)):
        prefix = prefix or 1
        suffix = suffix or 1
        prefix *= nums[i]
        suffix *= nums[len(nums) - 1 - i]
        max_product = max(prefix, suffix, max_product)
    return max_product


response = maxProductOptimal([0, 2, 3, -2, 4])
print(response)
