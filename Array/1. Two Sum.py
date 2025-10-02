# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]


def twoSum(nums: list[int], target: int) -> list[int]:
    hash_map = dict()
    for i, num in enumerate(nums):
        need = target - num
        if need in hash_map:
            return [hash_map[target - num], i]
        hash_map[num] = i


response = twoSum([2, 7, 11, 15], 6)
print(response)
