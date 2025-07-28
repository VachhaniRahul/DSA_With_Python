

# Chech whether given string is palindrome or not

# Example --> nitin  --> its reverse also read as nitin 


def palindrome(s,left = 0, right = None):
    if right is None:
            right = len(s) - 1
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return palindrome(s,left+1,right-1)

print(palindrome('nitin'))


# def palindrome(s):
#     if len(s) <= 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return palindrome(s[1:-1])

# print(palindrome('nitin'))