# Example 1:
# Image: https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1


# def maxArea(height: list[int]) -> int:
#     max_area = 0
#     for i in range(len(height)):
#         for j in range(i, len(height)):
#             h = min(height[i], height[j])
#             w = j - i
#             area = h * w
#             print(f"height:{h}x{w}={area}")
#             max_area = max(max_area, area)
#     return max_area


def maxAreaOptimal(height: list[int]) -> int:
    # Stores the maximum water area found so far
    max_area = 0
    # Two pointers: start from both ends of the array
    left = 0
    right = len(height) - 1
    # Continue until the pointers meet
    while left < right:
        # The container height is limited by the shorter line
        h = min(height[left], height[right])
        # Width is the distance between the two pointers
        w = right - left
        # Calculate the area with current left and right
        area = h * w
        # Update the maximum area if current area is larger
        max_area = max(max_area, area)
        # Move the pointer pointing to the shorter line
        # because moving the taller one won't increase height
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return max_area


response = maxAreaOptimal([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(response)
