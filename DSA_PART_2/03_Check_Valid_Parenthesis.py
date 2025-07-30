# Check_valid Parenthesis

s = '()[]{[]}'

def check_valid(s):
    d = {
        '}' : '{',
        ')' : '(',
        ']' : '['
    }

    l = []
    for i in s:
        if i in d:
            if l and l[-1] == d[i]:
               l.pop()
            else:
                return False
        else:
            l.append(i)
        
    return not(l)

print(check_valid(s))
