# In this you have to find how many plateform required to carry on all trains


arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]


trains = list(zip(arr, dep))
trains.sort(key = lambda x : (x[1], x[0]))
print(trains)

plateform_count = 0

d = {}


for arr_t, dep_t in trains:
    if not d:
        d[f'last_e_time_{plateform_count}'] = float('-inf')
        plateform_count += 1
        

    found = False
    for i,v in d.items():
        if arr_t > v:
            d[i] = dep_t
            found = True
            break
    
    if not found:
        d[f'last_e_time_{plateform_count}'] = dep_t
        plateform_count += 1
  

print(plateform_count)

         

# OPTIMAL SOLUTION t(n log n) s(1)
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]


arr.sort()
dep.sort()

count = maxi = 0
i = j = 0

while i < len(arr) and j < len(dep):
    if arr[i] <= dep[j]:
        count += 1
        maxi = max(maxi, count)
        i += 1
    else:
        count -= 1
        j += 1
    
print(maxi)
        
