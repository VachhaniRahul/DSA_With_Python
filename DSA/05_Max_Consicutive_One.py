
# a = [1,1,0,0,1,0,1,1,1,1,0,1,1]

# n = []

# c = 0
# for i in a:
#     if i == 1:
#         c = c + 1
#     elif c > 0:
#         n.append(c)
#         c = 0
# if c > 0:
#     n.append(c)

# max = 0

# for i in n:
#     if i > max:
#         max = i
# print(max)



# a = [1,1,0,0,1,0,1,1,0,1,1,1]

# max_count = 0
# current = 0

# for i in a:
#     if i == 1:
#         current += 1
#         max_count = max(max_count, current)
#     else:
#         current = 0

# print(max_count)




a = [1,1,0,0,0,1,0,0,1,1,1]
max_count = 0
cur_count = 0

for i in a:
    if i == 1:
        cur_count += 1
        max_count = max(max_count, cur_count)
    else:
        cur_count = 0

print(max_count)