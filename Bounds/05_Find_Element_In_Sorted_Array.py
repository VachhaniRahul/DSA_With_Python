

# WRITE A PROGRAM THAT GIVE TRUE IF ELEMENT PRESENT IN A SORTED ARRAY ELSE FALSE (ALSO PRESENT DUBLICATE ELEMENTS)


def find_element(arr, target):
    n = len(arr)
    left = 0
    right = n - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        if arr[mid] == arr[left] == arr[right]:
            left = left + 1
            right = right -1
        elif arr[mid] <= arr[right]:
            if arr[mid] <= target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if arr[left] <= target <= arr[mid]:
                right = mid - 1
            else:
                left = left + 1
    return False

a = [7, 7, 7, 1, 2, 7]
print(find_element(a, 1))