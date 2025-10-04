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
    prefix = 1
    postfix = 1
    max_prodcut = nums[0]
    for i in range(len(nums)):
        if prefix == 0:
            prefix = 1
        if postfix == 0:
            postfix = 1
        prefix *= nums[i]
        postfix *= nums[len(nums) - i - 1]
        local_max = max(prefix, postfix)
        max_prodcut = max(max_prodcut, local_max)
    return max_prodcut


response = maxProductOptimal([0, 2, 3, -2, 4])
print(response)
