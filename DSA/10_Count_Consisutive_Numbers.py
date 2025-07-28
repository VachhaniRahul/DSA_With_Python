
# # Example = [98,99,100,101]

a = [1, 99, 101, 98, 2, 5, 3, 100, 1, 1]

s = set(a)

longest = 0

for i in s:
    count = 0
    if i-1 not in s:
        count += 1
        j = i + 1
        while j in s:
            count +=1
            j += 1
    else:
        continue

    longest = max(longest, count)

print(longest)
    
    








    








