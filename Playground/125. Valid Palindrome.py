# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.


def isPalindrome(s: str) -> bool:
    s = "".join(c.lower() for c in s if c.isalnum())

    if s == s[::-1]:
        return True
    else:
        return False


def isPalindromeWithPointer(s: str) -> bool:
    s = "".join(c.lower() for c in s if c.isalnum())
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


print(isPalindrome("A man, a plan, a canal: Panama"))
