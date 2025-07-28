
# WRITE A PROGRAM TO FIND INDEX IN SORTED ROTATED ARRAY

def find_index(arr, target):
    n = len(arr)
    left , right = 0, n-1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        
        if arr[mid] <= arr[right]:
            if arr[mid] <= target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if arr[left] <= target <= arr[mid]:
                right = mid - 1
            else:
                left = mid + 1

    return -1

a = [10, 14,15,1,2,3,4]
print(find_index(a, 15))
