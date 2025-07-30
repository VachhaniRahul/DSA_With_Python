# Question: Find the Next Greater Element to the Right for each element in the list.
# If no greater element exists to the right, return -1 for that position.
# Approach: Use a monotonic decreasing stack while traversing from right to left.


a = [19, 4, 2, 11, 4, 5, 6, 10]
ans = [-1] * len(a)
stack = []

for i in range(len(a)-1, -1, -1):

    while stack and stack[-1] <= a[i]:
        stack.pop()

    if stack:
        ans[i] = stack[-1]
    
    stack.append(a[i])
    
print(ans)



