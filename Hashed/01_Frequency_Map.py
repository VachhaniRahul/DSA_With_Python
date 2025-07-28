
# Store the frequency in dictionary


nums = [5,6,7,7,1,9,111,1,1,5,1,1]
d = {}

for i in nums:
    d[i] = d.get(i,0) + 1

print(d)





# Using Counter
from collections import Counter
import time

nums = [5, 6, 7, 7, 1, 9, 111, 1, 1, 5, 1, 1]

start = time.time()  # Record start time
freq = Counter(nums)  # Run the operation
end = time.time()  # Record end time

print(f"Execution time: {end - start:.6f} seconds")
print(freq)




# start = time.time()  # Record start time

# for i in range(100000000):
#     pass
# end = time.time()  # Record end time
# print(f"Execution time: {end - start:.6f} seconds")
