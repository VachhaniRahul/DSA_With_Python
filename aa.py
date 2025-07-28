

# s = 'abc'
# result = []
# def backtrack(s, path='', use=set()):
#     if len(path) == len(s):
#         result.append(path)
#         return
       
#     m = len(s)
#     for i in range(m):
#         if i in use:
#             continue
#         use.add(i)
#         backtrack(s, path+s[i],use)
#         use.remove(i)


# backtrack(s)
# print(result)




# first_non_repeating("aabbccdeff")  # Output: 'd'
# first_non_repeating("aabbcc") 

# def first_non_repeating(s):
#     d = {}

#     for i in s:
#         d[i] = d.get(i, 0) + 1

#     a = None

#     for i,j in d.items():
#         if j == 1:
#             a = i
#             break
#     return a

# print(first_non_repeating('aabbccdeff'))
# print(first_non_repeating("aabbcc"))





# is_anagram("listen", "silent")  # Output: True
# is_anagram("hello", "world") 



# # Valid Parenthesis
# s = '(]'
# def valid(s):
#     d = {
#         ')' : '(',
#         '}' : '{',
#         ']' : '['
#     }

#     l = []

#     for i in s:
#         if i in d and len(l) > 0:
#             last = l.pop()
#             if last != d[i]:
#                 return False
#         elif i in d:
#             return False
#         else:
#             l.append(i)
#     return len(l) == 0

# print(valid(s))


# def sub1(s, start=0, end=0, sub='', result=[]):

#     if start == len(s):
#         return
    
#     if end == len(s) + 1:
#         sub1(s, start+1, start+1, sub='', result=result)
#     else:
#         if start < len(s) and end < len(s):
#             sub=s[start:end+1]
#             result.append(sub)
#         sub1(s, start, end+1, sub, result=result)  
        


# result = []
# sub1('abc', 0,0, result=result)
# print(result)




# a = 'abcdeafghi'


# i = 0
# j = 0
# maxi = 0
# d = {}

# while j<len(a):
#     if a[j] in d:
#         i = d[a[j]] + 1

#     maxi = max(maxi, j-i+1)
#     d[a[j]] = j 
#     j+=1
# print(maxi)
    


# a = 'abcdeafghij'

# i = 0
# j = 0
# maxi = 0
# d = {}

# while j < len(a):
#     if a[j] in d and d[a[j]] >= i:
#         i = d[a[j]] + 1

#     maxi = max(maxi, j - i + 1)
   
#     d[a[j]] = j 
#     j += 1

# print(maxi)



