nums = [2, 10, 12, 1, 11]
ans = [-1] * len(nums)

stack = []

# for i in range(len(nums)-1, -1, -1):
#     while stack and stack[-1] <= nums[i]:
#         stack.pop()
#     if stack:
#         ans[i] = stack[-1]
#     stack.append(nums[i])

# stack.reverse()

# for i,v in enumerate(ans):
#     if v == -1:
#         while stack and stack[-1] <= nums[i]:
#             if stack[-1] == nums[i]:
#                 break
#             stack.pop()
        
#         if stack and stack[-1] != nums[i]:
#             ans[i] = stack[-1]
# print(ans)



# OPTIMAL

# only imagine two times of arr we take but not actully taken space


for i in range(len(nums)*2-1, -1, -1):
    while stack and stack[-1] <= nums[i%len(nums)]:
        stack.pop()

    if i < len(nums):
        if stack:
            ans[i] = stack[-1]
    stack.append(nums[i%len(nums)])

print(ans)

