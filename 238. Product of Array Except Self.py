from typing import List

nums = [1, 2, 3, 4]


def productExceptSelf(nums: List[int]) -> List[int]:
    res = [1] * len(nums)
    left = [1] * len(nums)
    right = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        left[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        right[i] = postfix
        postfix *= nums[i]

    for i in range(len(nums)):
        res[i] = left[i] * right[i]
    return res


response = productExceptSelf(nums)
print(response)


# [1,2,3,4]
# prefix [1,1,2,6]
# posfix [24,12,4,1]
# output [24,12,8,6]

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
