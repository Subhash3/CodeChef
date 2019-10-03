#!/usr/bin/env python3
for i in range(int(input())) :
    vals = list(map(int, input().split()))
    quantity = vals[0]
    price = vals[1]
    expense = quantity * price
    if quantity > 1000 :
        expense = expense * 9 / 10
    print(expense)
