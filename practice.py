nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
r = 2 
maxi = 0
zeros = 0
left = 0
right = 0

while right < len(nums):
    if nums[right] == 0:
        zeros += 1

    while zeros > r:
        if nums[left] == 0:
            zeros -= 1
        left += 1

    maxi = max(maxi, right - left + 1)
    right += 1

print(maxi)
