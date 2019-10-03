#!/usr/bin/python3

def print_list(L) :
    for num in L :
        print(num, end=' ')
    print()

    return

try :
    T = int(input())
except :
    quit()

for testCase in range(T) :
    N = int(input())
    Arr = list(map(int, input().split()))
    B = list()
    for i in range(N) :
        count = 0
        for j in range(i+1, N) :
            if Arr[i] < Arr[j] :
                count += 1
        B.append(count)

    print_list(B)