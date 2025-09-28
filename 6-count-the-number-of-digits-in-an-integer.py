n = 123456789
num = n

# count = 0
# while num > 0:
#     num = num // 10
#     count = count + 1
# print(count)

from math import *


def countDigits(vnum):
    return int(log10(vnum) + 1)


resp = countDigits(num)
print(resp)
