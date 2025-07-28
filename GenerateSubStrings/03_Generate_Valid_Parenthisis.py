


# def per(n,index=0, open=None, close=None, sub=None):
#     if open is None and close is None:
#         open = close = n
#         print(open, close)
#     if sub is None:
#         sub = [""] * (n*2)

#     if index == (n*2):
#         result.append("".join(sub))
#         return
    
#     if open > 0:
#         sub[index] = "("
#         per(n, index+1, open-1, close, sub)
        
#     if close > open:
#         sub[index] = ')'
#         per(n, index+1, open, close-1, sub)

# result = []   
# per(2)
# print(result)









def generate_parentheses(n, open=0, close=0, path="", result=None):
    if result is None:
        result = []
    
    if len(path) == 2 * n:
        result.append(path)
        return result

    if open < n:
        generate_parentheses(n, open + 1, close, path + "(", result)
    
    if close < open:
        generate_parentheses(n, open, close + 1, path + ")", result)
    
    return result

# Example usage:
result = generate_parentheses(3)
print(result)







def generate(n,result, open=0, close=0, path=''):
    if len(path) == n * 2:
        result.append(path)
        return
    
    if open < n:
        generate(n, result, open+1, close, path+'(')
    if close < open:
        generate(n, result, open, close+1, path+')')

    
n = 1
r = []
generate(n,r)
print(r)
