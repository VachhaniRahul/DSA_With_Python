



# def rev_list(l):
#     if len(l) == 0:
#         return []
#     if len(l) == 1:
#         return l
    
#     return [l[-1]] + rev_list(l[:-1])

# print(rev_list([1,2,3]))



# Reverse the array with only given index range


def rev_arr(left, right, l=[]):
    if left >= right:
        return l
    l[left], l[right] = l[right], l[left]
    return rev_arr(left+1, right-1, l)

l1 = [1,2,3,4,5,6]
print(l1)
print(rev_arr(2,3,l1))
print(l1)


