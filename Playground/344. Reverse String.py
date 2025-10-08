# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

# You must do this by modifying the input array in-place with O(1) extra memory.


# In Python, methods that mutate (change) the object in place —
# like list.reverse(), list.sort(), list.clear(), list.append(), etc. —
# are designed to return None.
def reverseString(s: list[str]) -> None:
    s.reverse()
    print(s)


def reverseStringSwap(s: list[str]) -> None:
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    print(s)


print(reverseStringSwap(["H", "a", "n", "n", "a", "h"]))
