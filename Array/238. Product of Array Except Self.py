# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


def productExceptSelf(nums: list[int]) -> list[int]:
    leftTraverse = [1] * len(nums)
    rightTraverse = [1] * len(nums)
    res = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        leftTraverse[i] = prefix
        prefix *= nums[i]
    print(leftTraverse)

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        rightTraverse[i] = postfix
        postfix *= nums[i]
    print(rightTraverse)

    for i in range(len(nums)):
        res[i] = leftTraverse[i] * rightTraverse[i]

    return res


response = productExceptSelf([1, 2, 3, 4])
print(response)
