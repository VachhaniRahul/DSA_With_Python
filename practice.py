a = 'abd'
result = []

def backtrack(s, start=0, sub=[]):
    if start>=len(s):
        result.append(''.join(sub[:]))
        return
    sub.append(s[start])
    backtrack(s, start+1, sub)
    sub.pop()
    backtrack(s, start+1, sub)

backtrack(a)

print(sorted(result, key=lambda a: len(a)))
    
    
    
    
     
    
