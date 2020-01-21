#!/usr/bin/python3

try :
    T = int(input())
except :
    quit()

for testCase in range(T) :
    N = int(input())
    Arr = list()

    length = 0
    max_star = None
    for n in input().split() :
        star = 0
        num = int(n)
        Arr.append(num)
        length += 1
        for i in range(length-2, -1, -1) :
            if Arr[i]%num == 0:
                star += 1
        if max_star == None or max_star < star :
            max_star = star
    print(max_star)
