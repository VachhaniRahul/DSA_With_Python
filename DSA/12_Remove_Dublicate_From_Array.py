# REMOVE THE DUPLICATE FROM SOTRED ARRAY AND FIRST COME UNIQUE ELEMENTS IN PLACE

a = [1,1,1,2,2,2,3,3,3,4,4,4]

i = 0
j = i + 1
while j < len(a):
    if a[i] == a[j]:
        j += 1
    else:
        a[i+1] = a[j]
        i += 1
        j += 1

print(a)
