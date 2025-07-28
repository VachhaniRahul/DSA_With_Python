


# WRITE A PROGRAM THAT GIVE ALL THE COMBINATION OF THAT IS SUM = TARGET 
# WE CAN USE ONE NUMBER ANY TIME 

#[2,3,4,5] , TARGET = 8
# THEN WE CAN USE [2,2,2,2], [2,2,4], [4,4],[5,3]
result = []

def generate_com(nums,target,index=0,total=0, sub=None):
    if sub is None:
        sub = []

    if total > target:
        return
    if total == target:
        result.append(sub[:])
        return
    if index == len(nums):
        return
    
    sub.append(nums[index])
    generate_com(nums,target,index,total+nums[index],sub)
    sub.pop()
    generate_com(nums,target,index+1, total, sub)

nums = [2,3,6,7]
generate_com(nums,7)
print(result)
    







# WRITE A PROGRAM THAT HAVE DUBLICATE AND GIVE UNIQUE COMBINATION OF THAT SUM = TARGET

nums = [1, 1, 1, 2, 2]
total = 4
result = []

def backtrack(nums,index, total, sub=None):
    if sub is None:
        sub = []

    if total < 0:
        return
    
    if total == 0:
        result.append(sub[:])
        return
    
    for i in range(index, len(nums)):
        if i > index and nums[i-1] == nums[i]:
            continue

        sub.append(nums[i])
        backtrack(nums, i+1, total-nums[i], sub)
        sub.pop()

backtrack(nums,0,total)
print(result)






# WRITE A PROGRAM THAT WITH GIVE ALL POSSIBLE K LENGTH LIST WITH SUM = TARGET

target = 36
k = 6
result = []


def backtrack(target,index, k ,total, sub=None):
    if sub is None:
        sub = []

    if total > target:
        return

    if len(sub) == k:
        if total == target:
            result.append(sub[:])
        return
    
    for i in range(index,10):
        sub.append(i)
        backtrack(target,i+1, k, total+i, sub)
        sub.pop()

backtrack(target,1,k,0)
print(result)
    
    

        