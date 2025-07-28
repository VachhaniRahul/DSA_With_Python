
# Input: "leetcode"
# Output: 0

# Input: "loveleetcode"
# Output: 2

# Input: "aabb"
# Output: -1
     
s = 'loveleetcode'
d = {}


for i,v in enumerate(s):
    if v in d:
        d[v][1] += 1 
    else:
        d[v] = [i, 1]


for i in s:
    if d[i][1] == 1:
        print(d[i][0])
        break

else:
    print(-1)



