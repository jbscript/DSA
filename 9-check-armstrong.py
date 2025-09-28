# 153 1634
n = 1634

num = n
numlen = len(str(n))
total = 0
while num > 0:
    ld = num % 10
    total = total + (ld**numlen)
    num = num // 10

if n == total:
    print("Armstrong")
else:
    print("Not Armstrong")
