# Example 1:
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

# Example 2:
# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

# Example 3:
# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.


# Recursive fib fn
def fib(n: int) -> int:
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fib(n - 1) + fib(n - 2)


hash_map = {0: 0, 1: 1}


# DP fib fn
def fib_dp(n: int) -> int:
    if n in hash_map:
        return hash_map[n]
    hash_map[n] = fib_dp(n - 1) + fib_dp(n - 2)
    return hash_map[n]


# True DP fib fn
def fib_optimal(n: int) -> int:
    if n == 1:
        return 1
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(n - 1):
        c = a + b
        a = b
        b = c
    return c


import datetime

start = datetime.datetime.now()
# print(fib(40))
# print(fib_dp(500))
print(fib_optimal(15000))

end = datetime.datetime.now()
print(end - start)
