
# Factorial

# def fact(n):
#     if n < 0:
#         return 0
#     if n == 1 or n == 0:
#         return 1
#     return n * fact(n-1)

# print(fact(0))


# FIbbonacci 
# 0,1,1,2,3,5,8,13

def print_fibonacci(n, a=0, b=1, result = []):
 
    if n < 0:
        return result[-1]
    # print(a, end=' ')
    result.append(a)
    return print_fibonacci(n-1, b, a + b, result)

print(print_fibonacci(1))


# def fibbo(num):
#     if num == 0 or num == 1:
#         return num
#     return fibbo(num - 1) + fibbo(num - 2)

# print(fibbo(5))