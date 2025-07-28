# def kadane(arr):
#     max_sum = current_sum = arr[0]
#     for num in arr[1:]:
#         current_sum = max(num, current_sum + num)
#         max_sum = max(max_sum, current_sum)
#     return max_sum

# a = [-2, 1, -3, 4, -1, 2, 1, -5, 14]
# # print(kadane(a))  # Output: 15    # this is very optimal solution




a = [-2, 1, -3, 4, -1, 2, 1, -5, 14]

maximum = float('-inf')
length = len(a)

for i in range(length):
    total = 0
    for j in range(i, length):
        total += a[j]
        maximum = max(maximum, total)

print(maximum)





a = [-2, 1, -3, 4, -1, 2, 1, -5, 14]
max_sum = cur_sum = a[0]

for i in a[1:]:
    cur_sum = max(i, cur_sum+i)
    max_sum = max(max_sum, cur_sum)

print(max_sum)






# nums = [ 1, 2, 4, -15, 6, 3]

# max_sum = cur_sum = nums[0]
# start = end = s = 0
# for v,i in enumerate(nums[1:], start=1):
#     if i > (cur_sum+i):
#         cur_sum = i
#         s = v
#     else:
#         cur_sum += i
        
#     if cur_sum > max_sum:
#         max_sum = cur_sum
#         start = s
#         end = v

# print(max_sum, start, end)