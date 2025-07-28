n = 10


def convert_binary(n):
    output = ''
    while n > 0:
        o = n % 2
        output = str(o) + output
        n = n // 2
    return output

print(convert_binary(13))


def convert_int(n):
    n = str(n)
    total = 0
    for i, digit in enumerate(n[::-1]):
        total += int(digit) * (2 ** i)
    return total

print(convert_int(1001))




