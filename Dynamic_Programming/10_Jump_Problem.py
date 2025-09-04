# You are given an array of non-negative integers nums. Each element in the array represents your maximum jump length at that position.
# Return True if you can reach the last index, or False otherwise.



nums = [3, 2, 1, 4, 0, 2, 1, 5]


def canJump(nums):
    max_reach = 0
    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])
    return True

print(canJump(nums))




# find minimun jumps 
nums = [2, 3, 1, 4, 1, 1, 1, 2]

jump = 0

left = 0
right = 0

while right < len(nums)-1:
    farthest = 0
    for i in range(left, right+1):
        farthest = max(farthest, i+nums[i])
    left = right + 1
    right = farthest
    jump += 1

print(jump)
    
    

# BACKTRACKING
nums = [2, 3, 2, 0, 1, 4]

maxi = float('inf')

def backtrack(index=0, jump=0):
    if index >= len(nums)-1:
        global maxi
        maxi = min(maxi, jump)
        return 
    value = nums[index]
    for i in range(index+1, index+value+1):
        backtrack(i, jump+1)

backtrack()    
print(maxi)

    



    