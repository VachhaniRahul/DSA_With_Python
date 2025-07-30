s = 'a+(b)*(c-d)'

def priority(char):
    if char == '+' or char == '-':
        return 1
    if char == '*' or char == '/':
        return 2
    
    return 0

def infix_to_postfix(s):
    stack = []
    result = []

    for char in s:
        if ('a'<=char<='z') or ('A'<= char<= 'Z') or ('0' <= char <= '9'):
            result.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while stack and priority(stack[-1]) >= priority(char):
                result.append(stack.pop())
            stack.append(char)

    while stack:
        result.append(stack.pop())
        
    return ''.join(result)

print(infix_to_postfix(s))