#!/usr/bin/python3

try :
    T = int(input())
except :
    quit()

for testCase in range(T) :
    N, M = map(int, input().split())
    Arr = dict()
    i = 0
    l = 0
    flag = True
    for num in input().split() :
        # print(i, l)
        num = int(num)
        if num in Arr :
            Arr[num] += 1
        else :
            Arr[num] = 1
            l += 1
        if i%N == N-1:
            # print("After ", N, " values: ", i)
            if l != N :
                flag = False
                break
            i = -1
            l = 0
            Arr = dict()
        i += 1
    if flag :
        print("YES")
    else :
        print("NO")