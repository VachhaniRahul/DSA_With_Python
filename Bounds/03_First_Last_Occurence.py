

# WRITE A PROGRAM THAT RETURN FIRST AND LAST OCCURENCE OF THAT ELEMENT IN ARRAY IF NOT EXISTS THEN RETURN [-1,-1]


def lower_bound(arr, target):
    lb = -1
    left = 0
    right = len(arr) - 1
    

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            lb = mid
            right = mid - 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return lb


# UPPER BOUND

def upper_bound(arr, target):
    ub = -1
    left = 0
    right = len(arr) - 1
    

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            ub = mid
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return ub



def first_last_find(arr,target):
    first = lower_bound(arr, target)
    if first == -1:
        return [-1, -1]
    last = upper_bound(arr, target)
    return [first, last]


a = [2, 4, 8, 8, 9, 11, 14, 14, 14, 18, 20]
print(first_last_find(a, 14))
