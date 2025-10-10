# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true

# Example 5:
# Input: s = "([)]"
# Output: false


def isValid(s: str) -> bool:
    stack = []
    open_closure_map = {"(": ")", "[": "]", "{": "}"}
    for token in s:
        if token in open_closure_map:
            stack.append(token)
        else:
            if not stack or open_closure_map[stack.pop()] != token:
                return False
    return len(stack) == 0


print(isValid("()[]{}"))
