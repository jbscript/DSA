# 10 -> [1,2,5,10]
# 15 -> [1,3,5,15]

# n = 25
# num = n
# factors = []
# for i in range(1, n + 1):
#     if num % i == 0:
#         factors.append(i)
# print(factors)


# # Better Solution (we only need to check till num//2) since no number > num//2 can be a factor except num itself)
# n = 25
# num = n
# factors = []
# for i in range(1, n // 2):
#     if num % i == 0:
#         factors.append(i)
# factors.append(n)  # adding the number itself
# print(factors)

# optimized solution (we only need to check till sqrt(num))
from math import sqrt

n = 25
factors = []
for i in range(1, int(sqrt(n))):
    if n % i == 0:
        factors.append(i)
factors.append(n)  # adding the number itself
print(factors)
