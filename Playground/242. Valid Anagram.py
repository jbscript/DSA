# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

from collections import Counter


def isAnagramUsingBuiltInFn(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count = {}
    for c in s:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1

    for c in t:
        if c in count:
            count[c] -= 1
        else:
            count[c] = 1

    for value in count.values():
        if value != 0:
            return False
    return True


print(isAnagram("anagram", "nagaram"))
