#!/usr/bin/python3

try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    N = int(input())
    prices = list()
    length = 0
    count = 0
    for num in input().split() :
        n = int(num)
        prices.append(n)
        length += 1
        # print(n)
        flag = True
        for i in range(length-2, -1, -1) :
            if i == length-7 :
                break
            # print(prices[i], end=' ')
            if n >= prices[i] :
                flag = False
                break
        # print('\n')
        if flag :
            count += 1
    print(count)
