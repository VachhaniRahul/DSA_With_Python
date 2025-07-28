

# def insertion_sort(arr):
#     length = len(arr)
   
#     for i in range(1,length):
#         key = arr[i]

#         pos = i
#         for j in range(i-1, -1, -1):
#             if arr[j] > key:
#                 arr[j+1] = arr[j]
#                 pos = j
#             else:
#                 break
#         arr[pos] = key
#         print(arr)





# arr = [2,4,6,5,10,11,3]
# # insertion_sort(arr)
                



def insertion_sort(arr):
    length = len(arr)

    for i in range(length):
        key = arr[i]
        j = i-1
    
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key
        print(arr)


arr = [2,4,6,5,10,11,3]
insertion_sort(arr)     





        

            






