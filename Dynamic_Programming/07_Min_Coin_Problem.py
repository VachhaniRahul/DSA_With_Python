
coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]

n = 77
result = []

for i in range(len(coins)):
    if coins[i] > n:
        j = i - 1
        while j >= 0:
            if coins[j] <= n:
                result.append(coins[j])
                n = n - coins[j]
            else:
                j -= 1
        break

print(result)




# this is also good 
coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
n = 77
result = []

# Start from the largest coin
for i in range(len(coins)-1, -1, -1):
    while n >= coins[i]:
        n -= coins[i]
        result.append(coins[i])

print(result)  # Output: [50, 20, 5, 2]
