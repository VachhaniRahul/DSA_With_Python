
def add(n):
    if n <= 0:
        return 0
    return n + add(n-1)

print(add(10))


def add(i,j, sum=0):

    if i > j:
        return sum
    return add(i+1,j,sum+i)

print(add(100,110))