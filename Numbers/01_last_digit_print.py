
# (1) Print the digit from last

n = 5873
num = n

while num != 0:
    last_digit = num % 10
    num = num // 10
    print(last_digit)


