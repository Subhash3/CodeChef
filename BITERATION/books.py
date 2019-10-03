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
    Arr = dict()
    length = 0
    for num in input().split() :
        num = int(num)
        if num in Arr :
            Arr[num] += 1
        else :
            length += 1
            Arr[num] = 1
    print(Arr)
    B = list()
    sum_of_counts = N
    j = 0
    for num, count in Arr.items() :
        print(num, count)
        sum_of_counts -= count
        B.append(sum_of_counts)
        j += 1
    while j < N :
        B.append(0)
        j += 1
    print_list(B)