#!/usr/bin/python3

try :
    T = int(input())
except :
    quit()

arr = dict()
for testCase in range(T) :
    val = list(map(int, input().split()))
    choice = val[0]


    if choice == 1 :
        L = val[1]
        R = val[2]
        D = val[3]

        for i in range(L, R+1) :
            if i not in arr :
                arr[i] = D
            else :
                arr[i] += D
            print(arr)
    if choice == 2 :
        position = val[1]
        print(arr[position])