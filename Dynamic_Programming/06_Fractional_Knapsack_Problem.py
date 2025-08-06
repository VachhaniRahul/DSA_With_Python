arr = [(100, 20), (60, 10), (100, 50), (200, 50)]
w = 100
arr.sort(key=lambda x: x[0]/x[1], reverse=True)


total = 0

for i,j in arr:
    if w >= j:
        total += i
        w -= j
    else:
        rem = (i / j) * w
        total += rem
        break
print(total)