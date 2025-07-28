
# Print all the factor of the given number

# Example --> 9 --> 1, 3, 9


num = 91

factors = set()
for i in range(1,int(num ** 0.5)+1):
    if num % i == 0:
        factors.add(i)
        factors.add(num // i)
factors = sorted(factors)

print(factors)
    



# # Recursion approach

# def find_factors(num, i=1, factors=None):
#     if factors is None:
#         factors = []

#     if i > num // 2:
#         factors.append(num)  # add the number itself at the end
#         return factors

#     if num % i == 0:
#         factors.append(i)

#     return find_factors(num, i + 1, factors)

# # Test
# num = 1921
# result = find_factors(num)
# print(result)