
def merge_two_list_without_repeat(arr1, arr2):
    left, right = 0, 0
    arr1_len , arr2_len = len(arr1), len(arr2)
    result = []

    while left < arr1_len and right < arr2_len:
        if len(result) > 0 and arr1[left] == result[-1]:
            left += 1
        elif len(result) > 0 and arr2[right] == result[-1]:
            right += 1
        elif arr1[left] == arr2[right]:
            result.append(arr1[left])
            left +=1
            right+=1
        elif arr1[left] < arr2[right]:
            result.append(arr1[left])
            left += 1
        else:
            result.append(arr2[right])
            right+=1
    
    while left < arr1_len:
        if len(result) > 0 and arr1[left] != result[-1] or len(result) == 0:
            result.append(arr1[left])
            left += 1
        else:
            left += 1
            
    
    while right < arr2_len:
        if len(result) > 0 and arr2[right] != result[-1] or len(result) == 0:
            result.append(arr2[right])
            right += 1
        else:
            right += 1


    print(result)
    

  
arr1 = [10,20,20,20,30]
arr2 = [20,40,60,60]
merge_two_list_without_repeat(arr1,arr2)