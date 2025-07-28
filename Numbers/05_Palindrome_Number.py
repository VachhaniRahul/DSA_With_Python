
# Check the number is palindrome or not

# example --> 121  is palindrone 


n = 1
num = n
rev = 0

while num > 0:
    last_digit = num % 10 
    rev = rev * 10 + last_digit
    num = num // 10

if n == rev:
    print('The number is palindrome')
else:
    print('The number is not palindrome')
