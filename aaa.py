
# a = 'abcdeafghik'
# a = 'aabb'
a = 'pwwkew'
d = {}
maxi = 0
i = 0
j = 0
result = ''

while j < len(a):
    if a[j] in d and d[a[j]] >= i:
        i = d[a[j]] + 1

    maxi = max(maxi, j - i +1)
    if maxi == j - i +1 and len(result) < maxi:
        result = a[i : j+1]
    d[a[j]] = j
    j+=1

print(maxi)
print(result)



class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j = 0,0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i+=1
            j+=1
        return i == len(s)
    
s = Solution()
print(s.isSubsequence('a', 'abcdefg'))
