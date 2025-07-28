
# a = [10, 30, 50, 90]
# target = 80

# d = {}
 

# for i in range(len(a)):
#     new_target = target - a[i]
#     if new_target in d and d[new_target] != i:
#         print([d[new_target], i])
#         break
#     d[a[i]] = i



# a = [10,20,40,80]
# target = 60

# d = {}

# for i in range(len(a)):
#     new_target = target - a[i]
#     if new_target in d and d[new_target] != i:
#         print([d[new_target], i])
#         break
#     d[a[i]] = i
 









# a = [10,30,60,70]
# target = 80
# d = {}

# for i in range(len(a)):
#     r_t = target - a[i]
#     if r_t in d and d[r_t] != i:
#         print(d[r_t], i)
#         break
#     d[a[i]] = i











a = [25,30,50,100]
tar = 130

d = {}

for i in range(len(a)):
    rem = tar - a[i]
    if rem in d and d[rem] != i:
        print([d[rem], i])
        break
    d[a[i]] = i











