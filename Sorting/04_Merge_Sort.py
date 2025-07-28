

def merge_arr(arr1, arr2):
    left = 0
    right = 0
    n,m = len(arr1),len(arr2)
    result = []
    
    while left < n and right < m:
        if arr1[left] < arr2[right]:
            result.append(arr1[left])
            left+=1
        else:
            result.append(arr2[right])
            right+=1

    while right < m:
        result.append(arr2[right])
        right+=1
    
    while left < n:
        result.append(arr1[left])
        left+=1

    return result

arr1 = [1,2,6,9]
arr2 = [1,2,5,7]

print(merge_arr(arr1,arr2))

def divide(arr):
    
    length = len(arr)
    if length <= 1:
        return arr
    length = length // 2
    left = arr[:length]
    right = arr[length:]
    sorted_left = divide(left)
    sorted_right = divide(right)
    return merge_arr(sorted_left, sorted_right)

    

arr = [1,6,7,4,5]
print(divide(arr))