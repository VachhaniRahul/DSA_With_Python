# nums = [6, 2, 3, 4, 2]
# k = 3
# maxi = 0

# def backtrack(nums, k, left_picked=0, right_picked=0):
#     global maxi
#     if left_picked + right_picked == k:
#         total = sum(nums[:left_picked]) + sum(nums[len(nums)-right_picked:])
#         maxi = max(maxi, total)
#         return

#     # Pick from left
#     backtrack(nums, k, left_picked + 1, right_picked)
    
#     # Pick from right
#     backtrack(nums, k, left_picked, right_picked + 1)

# backtrack(nums, k)
# print(maxi)




nums = [2, 1, 5, 4, 0, 10, 1]
k = 3
n = len(nums)
left_sum = 0
right_sum = 0

for i in range(0, k):
    left_sum += nums[i]

maxi = left_sum
right_index = n-1

for i in range(k-1, -1, -1):
    left_sum -= nums[i]
    right_sum += nums[right_index]
    right_index -= 1
    maxi = max(maxi, left_sum+right_sum)

print(maxi)

