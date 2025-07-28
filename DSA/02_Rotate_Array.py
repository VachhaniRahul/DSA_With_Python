
#  Rotate array in place

# arr = [10,20,30,40,50]

# arr1 = [arr[-1]]+arr[:-1]
# print(arr1)
# print(arr is arr1)

# arr = [10,20,30,40,50]

# arr[:] = [arr[-1]]+arr[:-1]
# print(arr)
# print(arr is arr)




# def rotate_arr(arr, k=1):
#     if k == 0:
#         return
#     length = len(arr)
#     last_digit = arr[length-1]
#     for i in range(length-2,-1,-1):
#         arr[i+1] = arr[i]
#     arr[0] = last_digit

#     rotate_arr(arr, k-1)

# arr = [10,20,30,40]
# rotate_arr(arr, 2)
# print(arr)
    

def rotate_arr(arr, k=1):
    n = len(arr)
    k = k % n  # In case k > n

    # Helper to reverse a portion of the list
    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    # Reverse entire array
    reverse(0, n - 1)
    # Reverse first k elements
    reverse(0, k - 1)
    # Reverse remaining elements
    reverse(k, n - 1)

arr = [10,20,30,40]
rotate_arr(arr, 2)
print(arr)
