

def selection_sort(arr):
    length = len(arr)
    for i in range(length-1):
        min_index = i
        for j in range(i+1,length):
            if arr[min_index] > arr[j]:
                min_index = j

        if i != min_index:
            arr[min_index],arr[i] = arr[i],arr[min_index]
        print(arr)

arr = [3,2,5,1,10,0]
selection_sort(arr)








# USING RECURSION
# def selection_sort(arr, start=0):
#     if start >= len(arr)-1:
#         return
    
#     min_index = start
#     for i in range(min_index+1,len(arr)):
#         if arr[i] < arr[min_index]:
#             min_index = i

#     arr[min_index],arr[start] = arr[start],arr[min_index]
#     print(arr)
#     selection_sort(arr, start+1)

# selection_sort(arr)