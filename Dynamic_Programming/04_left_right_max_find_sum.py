nums = [6, 2, 3, 4, 2]
k = 3
maxi = 0

def backtrack(nums, k, left_picked=0, right_picked=0):
    global maxi
    if left_picked + right_picked == k:
        total = sum(nums[:left_picked]) + sum(nums[len(nums)-right_picked:])
        maxi = max(maxi, total)
        return

    # Pick from left
    backtrack(nums, k, left_picked + 1, right_picked)
    
    # Pick from right
    backtrack(nums, k, left_picked, right_picked + 1)

backtrack(nums, k)
print(maxi)
