
# Check the number is armstrong number or not

# Example --> 153 

n = 1634
num = n
temp = num
sum = 0
count = 0

while num > 0:
    num = num // 10
    count += 1

# # Step 1: Count digits
# count = len(str(n))

while temp > 0:
    last_digit = temp % 10
    sum  = sum + (last_digit ** count)
    temp = temp // 10

if sum == n:
    print('The number is armstrong number')
else:
    print('The number is not armstrong number')
