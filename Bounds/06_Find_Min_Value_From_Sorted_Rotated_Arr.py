

# WRITE A PROGRAM TO FIND MIN VALUE FROM SORTED ROTATED ARRAY


def find_min_value(arr):
    n = len(arr)
    left = 0
    right = n - 1
    min_value = float('inf')

    while left <= right:
        mid = (left + right) // 2
        min_value = min(min_value, arr[mid])
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid - 1 
           
    return min_value

a = [6, 7, 8, 2, 3, 4, 5]
# a = [8,4,5,6,7]
# a = [1,2,3,4,5]
print(find_min_value(a))



