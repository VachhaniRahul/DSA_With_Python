
a = [-1, 0, 1, 1, 2, -1, -4]
a.sort()

length = len(a)

result = []

for i in range(length):
    if i > 0 and a[i] == a[i-1]:
            continue

    for j in range(i+1, length):

        l = j + 1
        k = length - 1

        while l < k:
            s = a[i] + a[j] + a[k] + a[l]
            if s == 0:
                result.append([a[i], a[j], a[l], a[k]])
                l += 1
                k -= 1

                while l < k and a[l] == a[l - 1]:
                    l += 1
                while l < k and a[k] == a[k + 1]:
                    k -= 1

            elif s > 0:
                k -= 1
            else:
                l += 1

print(result)