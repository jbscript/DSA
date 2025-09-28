n = 12221

num = n
reverse = 0

while num > 0:
    last_digit = num % 10
    reverse = (reverse * 10) + last_digit
    num = num // 10
if n == reverse:
    print("Palindrome")
else:
    print("Not Plaindrome")

# 121
# 121%10 -> 1
# 121//10 -> 12
# 12%10 -> 2
