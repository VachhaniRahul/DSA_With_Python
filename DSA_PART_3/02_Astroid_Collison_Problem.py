# Question: Simulate asteroid collisions.
# Positive numbers move right, negative numbers move left.
# When two meet:
# 1) Smaller magnitude asteroid is destroyed.
# 2) If equal magnitude, both are destroyed.
# Return the remaining asteroids after all collisions.


nums = [4, 7, 1, 1, 2, -3, -7, 17, 15, -16]

l = []

for num in nums:
    if not l:
        l.append(num)
    elif (l[-1] > 0 and num > 0) or (l[-1] < 0 and num < 0):
        l.append(num)
    else:
        ele = abs(num)
        while l and ele > abs(l[-1]):
            l.pop()
        if l and ele == abs(l[-1]):
            l.pop()
        elif not l:
            l.append(num)

print(l)
