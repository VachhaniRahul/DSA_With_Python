

# # WRITE A PROGRAM THAT GENERATE ALL THE SUB SEQUENCES 
# # EXAMPLE [1,2,3] --> [], [1],[2],[3],[1,2],[1,3],[1,2,3] ETC...


# nums = [1, 2, 3]

# result = []

# def sub_sequence(index=0, subset = []):

#     if index == len(nums):
        
#         print(subset)
#         result.append(subset[:])
#         return
    
#     subset.append(nums[index])
#     sub_sequence(index+1, subset, )
#     subset.pop()
#     sub_sequence(index+1, subset, )

# sub_sequence()

# print('Result -->', sorted(result, key=lambda x: len(x)))






# WRITE A PROGRAM THAT PRINT ALL THE SUBSEQUECE WHICH HAVE == SUM WITH TARGET


    
nums = [5, 4, 6, 3, 9,10,1]
target = 19

result = []

def sub_sequence(index=0, total=0, subset = []):

    if index == len(nums):
        if total == target:
            print(subset)
            result.append(subset[:])
        return
    if total > target:
        return
    
    subset.append(nums[index])
    sub_sequence(index+1, total+nums[index], subset)
    subset.pop()
    sub_sequence(index+1, total, subset )

sub_sequence()

print('Result -->', sorted(result, key=lambda x: len(x)))

