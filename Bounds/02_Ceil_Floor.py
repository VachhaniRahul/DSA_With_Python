
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    ceil = -1
    floor = -1
       

    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            return [arr[mid], arr[mid]]
        elif target < arr[mid]:
            ceil = arr[mid]
            right = mid - 1
        else:
            floor = arr[mid]
            left = mid + 1

    return [floor, ceil]

a = [2, 4, 8, 9, 11, 14, 18, 20]
print(binary_search(a,10))