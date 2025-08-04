# Question: Find the length of the longest substring without repeating characters.
# Approach: Sliding window with a hash map to store the last seen index of each character.
# Move the right pointer `j` through the string:
#   - If a character repeats inside the current window, move the left pointer `i` after the last occurrence.
#   - Track the maximum window size as we go.


s = 'pwwkew'
i, j = 0, 0
maxi = 0
d = {}

while j < len(s):
    if s[j] in d and d[s[j]] >= i:
        i = d[s[j]] + 1 
    
    maxi = max(j - i + 1, maxi)  
    d[s[j]] = j                  
    j += 1

print(maxi)
