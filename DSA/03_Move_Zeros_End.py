

# def move_zeros(arr):
#     length = len(arr)
#     new_arr = []
#     for i in arr:
#         if i != 0:
#             new_arr.append(i)
#     while len(new_arr) < length:
#         new_arr.append(0)
#     return new_arr


# arr = [1,2,0,1,0,4,0]
# print(move_zeros(arr)) 


def move_zeros(arr):
    pos = 0 

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[pos] = arr[i]
            pos += 1

    for i in range(pos, len(arr)):
        arr[i] = 0

arr = [1,2,0,1,0,4,0]
move_zeros(arr)
print(arr)