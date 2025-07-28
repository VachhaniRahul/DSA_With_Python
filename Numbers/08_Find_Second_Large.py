
# arr = [50,10,30,20,50]

# max = arr[0]

# second_max = None

# for i in range(1,len(arr)):
#     if arr[i] > max:
#         second_max = max
#         max = arr[i]
#     elif arr[i] != max:
#         if second_max is None or arr[i] > second_max:
#             second_max = arr[i]

# print(second_max)




arr = [50,10,30,20,50]

max = arr[0]

second_max = float('-inf')  

for i in range(1,len(arr)):
    if arr[i] > max:
        second_max = max
        max = arr[i]
    elif arr[i] > second_max and arr[i] != max:
        second_max = arr[i]

print(second_max)