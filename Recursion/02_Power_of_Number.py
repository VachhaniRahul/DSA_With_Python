

def power(num, n):
    if n == 0:
        return 1
    if n == 1:
        return num
    return num * power(num, n-1)

print(power(1,10))