

# def bubble_sort(arr):
#     length = len(arr)
#     for i in range(length-1): 
#         swap = False
#         for j in range(length-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j+1],arr[j] = arr[j],arr[j+1]
#                 swap = True
#         if not swap:
#             break
#         print(arr)

# arr = [1,5,2,0,3]
# bubble_sort(arr)
    


def bu_sort(arr):
    length = len(arr)
    for i in range(length-1):
        swap = False
        for j in range(length-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swap = True
        if not swap:
            break
        print(arr)


arr = [1,10,5,2,0,3]
bu_sort(arr)



                

