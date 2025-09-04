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



    



def asteroidCollision(asteroids):
    l = []

    for i in asteroids:
        alive = True

        while alive and i < 0 and l and l[-1] > 0:
            if abs(i) > abs(l[-1]):
                l.pop()
            elif abs(i) == abs(l[-1]):
                l.pop()
                alive = False
            else:
                alive = False
        if alive:
            l.append(i)
    return l
print(asteroidCollision(nums))






nums = [-7, 1, 1, 2, -3, -7, 17, 15, -16]
stack = []

for i in nums:
    if not stack:
        stack.append(i)
    elif (stack[-1] > 0 and i > 0) or (stack[-1] < 0 and i < 0):
        stack.append(i)
    else:
        if stack[-1] > 0:
            while stack and stack[-1] > 0 and stack[-1] < abs(i):
                stack.pop()
            if stack and stack[-1] > 0 and stack[-1] == abs(i):
                stack.pop()
            elif not stack or (stack and stack[-1] < 0):
                stack.append(i)
        else:
            stack.append(i)
print(stack)
            
