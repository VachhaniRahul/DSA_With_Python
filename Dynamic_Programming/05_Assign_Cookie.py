# Problem: Assign Cookies to Children
# -----------------------------------
# You are given two integer arrays:
#   1. greed[i] -> the greed factor of the i-th child (minimum cookie size the child needs)
#   2. s[j] -> the size of the j-th cookie available
#
# Rules:
# 1. A child is satisfied if they are given a cookie with size >= their greed.
# 2. Each cookie can be used to satisfy at most one child.
# 3. Your goal is to maximize the number of satisfied children.
#
# Return the maximum number of children that can be satisfied.
#
# Example:
# Input:  greed = [2, 3, 8, 1, 4],  s = [4, 2, 7, 1, 2, 3]
# Output: 4
#
# Explanation:
#  - Sort greed -> [1, 2, 3, 4, 8]
#  - Sort cookies -> [1, 2, 2, 3, 4, 7]
#  - Assign cookies in order:
#       1 -> 1 ✅
#       2 -> 2 ✅
#       3 -> 3 ✅ (skip smaller 2)
#       4 -> 4 ✅
#       8 -> 7 ❌
#  Maximum satisfied children = 4

greed = [2, 3, 8, 1, 4]
s = [4, 2, 7, 1, 2, 3]

greed.sort()
s.sort()

left = 0
right = 0
count = 0

while left < len(greed) and right < len(s):
    if s[right] >= greed[left]:
        count += 1
        left += 1
        right += 1
    else:
        right += 1

print(count)  # Output: 4
