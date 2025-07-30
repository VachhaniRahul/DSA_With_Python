

d = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


digit = "234"
result = []

def backtrack(index, digit, sub=None):
    if sub is None:
        sub = ''
    
    if index == len(digit):
        result.append(sub)
        return
    
    num = d[digit[index]]
    for i in num:
        backtrack(index+1, digit, sub+i)

    
backtrack(0,digit)
print(result)



# a = ['']
# s = '23'
# for i in s:
#     val = d[i]

#     new = []
#     for j in a:
#         for k in val:
#             new.append(j+k)
    
#     a = new

# print(a)

