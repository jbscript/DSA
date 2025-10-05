# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Example 3:
# Input: nums = [1], target = 0
# Output: -1


def search(nums: list[int], target: int) -> int:
    # Initialize the search boundaries
    left = 0
    right = len(nums) - 1

    # Step 1: Find the pivot (index of the smallest element)
    while left < right:
        mid = (left + right) // 2
        # If middle element is greater than the rightmost element,
        # the smallest element is to the right of mid
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            # Otherwise, the smallest element is at mid or to the left
            right = mid
    pivot = left  # Pivot index found

    # Step 2: Determine in which subarray to search for the target
    if nums[pivot] <= target <= nums[-1]:
        # If target is between pivot and end, search in the right subarray
        left = pivot
        right = len(nums) - 1
    else:
        # Otherwise, search in the left subarray (from start to pivot-1)
        left = 0
        right = pivot - 1

    # Step 3: Standard binary search in the chosen subarray
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid  # Target found
        elif nums[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half

    return -1  # Target not found


response = search([4, 5, 6, 7, 0, 1, 2], 2)
print(response)
