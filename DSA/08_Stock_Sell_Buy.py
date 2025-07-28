
# price = [7, 2, 1, 5, 6, 4, 8]
price = [7, 2, 1, 5, 6, 4, 8]

length = len(price)

min_price = float('inf')
max_profit = 0
for i in price:
    if i < min_price:
        min_price = i
    if(i - min_price) > max_profit:
        max_profit = i - min_price

print(min_price)
print(max_profit)



