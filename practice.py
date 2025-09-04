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




def longest_zero_sum_subarray(arr):
    prefix_sum = 0
    seen = {0: -1}  # prefix_sum: first index
    max_len = 0

    for i, num in enumerate(arr):
        prefix_sum += num
        if prefix_sum in seen:
            max_len = max(max_len, i - seen[prefix_sum])
        else:
            seen[prefix_sum] = i

    return max_len

# Test
a = [15, -2, 2, -8, 1, 7, 10, 23]
print(longest_zero_sum_subarray(a))  # Output: 5

