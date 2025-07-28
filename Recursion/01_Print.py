
# print hello 4 times

# def hello(n):
#     if n <= 0:
#         return
#     print('hello')
#     hello(n-1)

# hello(5)




# Head recursion --> function called its self after performimg task
# Tail recursion --> function called its self before performimg task



# # Head Recursion
# def hello1(n):
#     if n <= 0:
#         return
#     print(f'hello {n} time')
#     hello1(n-1)

# hello1(3)



# # Tail Recursion
# def hello1(n):
#     if n <= 0:
#         return
#     hello1(n-1)
#     print(f'hello {n} time')

# hello1(3)



# # Print 1 to N

def print_1_to_N(i,n):
    if i > n:
        return
    print(i)
    print_1_to_N(i+1,n)

print_1_to_N(1,5)
