
# Count the digit in given number


n = 234324
count = 0

if n == 0:
    count = 1
else:
    while n > 0:
        n = n // 10
        count += 1

print(count)  

    
    
# Time Compplexity  --> log₁₀(n)    --> log 10 because we divide the number by 10 so iteration depend on the 10 and length of number
# if we divide by 2 then its become log2(n)