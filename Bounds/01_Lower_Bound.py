

# LOWER BOUND


# This is q question for find the index when you can insert a target element in which index if already target is exists then return that index.
# Search Insert Position

def lower_bound(arr, target):
    lb = len(arr)
    left = 0
    right = len(arr) - 1
    

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            lb = mid
            right = mid - 1
        else:
            left = mid + 1

    return lb

a = [2, 4, 8, 9, 11, 14, 14, 14, 18, 20]
print(lower_bound(a,14))
# print(binary_search(a,10))





# UPPER BOUND

def upper_bound(arr, target):
    ub = len(arr)
    left = 0
    right = len(arr) - 1
    

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            ub = mid
            right = mid - 1
        else:
            left = mid + 1

    return ub

a = [2, 4, 8, 8, 9, 11, 14, 14, 14, 18, 20]
print(upper_bound(a,21))












