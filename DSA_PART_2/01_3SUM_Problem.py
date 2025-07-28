# This Python code attempts to solve the 3Sum problem, where you want to find all unique triplets in the array that sum to zero.


# a = [-1, 0, 1, 2, -1, -4]

# length = len(a)
# result = set()

# for i in range(length):
#     s1 = set()
#     for j in range(i+1,length):
#         rem_sum = -(a[i]+a[j])
#         if rem_sum in s1:
#             l1 = [a[i], a[j], rem_sum]
#             l1.sort()
#             result.add(tuple(l1))
#         s1.add(a[j])

# print(result)





# OPTIMAL 


a = [-1, 0, 1, 2, -1, -4]
a.sort()

length = len(a)

result = []

for i in range(length):

    if i > 0 and a[i] == a[i-1]:
        continue  # Skip duplicates for the first element

    j = i + 1
    k = length - 1

    while j < k:
        s = a[i] + a[j] + a[k]
        if s == 0:
            result.append([a[i], a[j], a[k]])
            j += 1
            k -= 1

            while j < k and a[j] == a[j - 1]:
                j += 1
            while j < k and a[k] == a[k + 1]:
                k -= 1

        elif s > 0:
            k -= 1
        else:
            j += 1

print(result)

        



