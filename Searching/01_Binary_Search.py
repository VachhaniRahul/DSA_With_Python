
# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1
    

#     while left <= right:
#         mid = (left + right) // 2
#         if target == arr[mid]:
#             return mid
#         elif target < arr[mid]:
#             right = mid - 1
#         else:
#             left = mid + 1

#     return -1

# a = [2, 4, 8, 9, 11, 14, 18, 20]
# print(binary_search(a,14))







# USING RECURSION





def binary_ser(arr, target, left=None,right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(arr)-1

    if left > right:
        return -1 

    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_ser(arr, target, left, right=mid-1)
    else:
        return binary_ser(arr, target, left=mid+1, right=right)
 
a = [2, 4, 8, 9, 11, 14, 18, 20]
print(binary_ser(a,11))
