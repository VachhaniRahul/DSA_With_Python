# You are given an integer array nums.
# Find the length of the longest contiguous subarray that contains at most 2 distinct numbers.


#Longest Subarray with At Most 2 Distinct Integers
# (Also called “Fruit Into Baskets” on LeetCode)



nums  = [3, 3, 2, 1, 1, 2, 3, 3, 4]

maxi = 0
d = {}
i = 0

for j in range(len(nums)):
    d[nums[j]] = d.get(nums[j], 0) + 1

    while len(d) > 2:
        d[nums[i]] -= 1
        if d[nums[i]] == 0:
            del d[nums[i]]
        i += 1
    
    maxi = max(maxi, j - i + 1)
 
print(maxi)