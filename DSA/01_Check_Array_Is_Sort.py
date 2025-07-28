
arr = [10,20,40,30]

sort = True

for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        sort = False
        break
print(sort)
    


# is_sorted = all(arr[i] <= arr[i+1] for i in range(len(arr) - 1))

# print(is_sorted)





