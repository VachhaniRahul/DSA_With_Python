
# arr = [10,20,-30,40,-1,-4]
# pos_arr = []
# neg_arr = []
# new_arr = []

# for i in arr:
#     if i > 0:
#         pos_arr.append(i)
#     else:
#         neg_arr.append(i)

# i = 0

# while i < (len(arr)//2):
#     new_arr.append(pos_arr[i])
#     new_arr.append(neg_arr[i]) 
#     i += 1
# print(new_arr)
    




# OPTIMAL SOLUTION

arr = [10,20,-30,40,-1,-4]
new_arr = [0 for i in range(len(arr))]
pos = 0
neg = 1

for i in arr:
    if i > 0:
        new_arr[pos] = i
        pos += 2
    else:
        new_arr[neg] = i
        neg += 2
    
print(new_arr)