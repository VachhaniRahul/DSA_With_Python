# # N Meeting in one room 

# start =  [0, 3, 1, 6, 7, 11]
# end   =  [6, 5, 2, 8, 10, 15]

# arr = list(zip(start,end))
# arr.sort(key=lambda x : (x[1], x[0]))
# print(arr)

# last = 0
# count = 0
# for i,j in arr:
#     if i >= last:
#         count += 1
#         last = j

# print(count)




start = [0, 3, 1, 6, 7, 11]
end = [6, 5, 2, 8, 10, 15]

meetings = list(zip(start, end))
meetings.sort(key=lambda x: x[1])
maxi = 0
mini = 0
last_e_time = float('-inf')

for s_time, e_time in meetings:
    if s_time > last_e_time:
        maxi += 1
        last_e_time = e_time
    else:
        # This is unselected meetings count
        mini += 1

print(maxi, mini)
