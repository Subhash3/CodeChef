#!/usr/bin/python3

def median(a, b, c) :
    if a > b:
        if a < c:
            median = a
            index = 0
        elif b > c:
            median = b
            index = 1
        else:
            median = c
            index = 2
    else:
        if a > c:
            median = a
            index = 0
        elif b < c:
            median = b
            index = 1
        else:
            median = c
            index = 2
    return index

try :
    T = int(input())
except :
    quit()

for testCase in range(T) :
    N = int(input())
    Arr = list(map(int, input().split()))
    length = N
    while length >= 3 :
        a = Arr[0]
        b = Arr[1]
        c = Arr[2]
        index = median(a, b, c)
        Arr.pop(index)
        length -= 1
    for num in Arr :
        print(num, end=' ')
    print()
