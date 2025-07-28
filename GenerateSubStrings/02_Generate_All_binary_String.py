
n = 4
result = []

def binary_string(index=0, flag=True, sub=[0 for i in range(n)]):
    if index == n:
        a = ""
        for i in sub:
            a = a + str(i)
        result.append(a)
        return
    if flag:
        sub[index] = 1
        binary_string(index+1, False, sub)
        sub[index] = 0
        binary_string(index+1, True, sub)
    else:
        binary_string(index+1, True, sub)

binary_string()
print(result)







n = 4
result = []

def binary_string(index=0, flag=True, sub=[0 for i in range(n)]):
    if index == n:
        a = ""
        for i in sub:
            a = a + str(i)
        result.append(a)
        return
    
    sub[index] = 0
    binary_string(index+1, True, sub)

    if flag:
        sub[index] = 1
        binary_string(index+1, False, sub)
        

binary_string()
print(result)