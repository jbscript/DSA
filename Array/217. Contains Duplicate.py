# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation: The element 1 occurs at the indices 0 and 3.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation:All elements are distinct.

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true


def containsDuplicateUsingHash(nums: list[int]) -> bool:
    hash_map = dict()
    for num in nums:
        if num in hash_map:
            return True
        hash_map[num] = 1
    return False


def containsDuplicateUsingSet(nums: list[int]) -> bool:
    nums_set = set(nums)
    if len(nums) > len(nums_set):
        return True
    return False


response = containsDuplicateUsingSet([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
print(response)
