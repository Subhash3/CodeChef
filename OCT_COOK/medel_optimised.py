#!/usr/bin/python3

try :
    T = int(input())
except :
    quit()

for testCase in range(T) :
    N = int(input())
    Arr = list(map(int, input().split()))
    smaller = None
    larger = None
    for i in range(N) :
        num = Arr[i]
        if smaller == None or num < smaller :
            smaller = num
        if larger == None or num > larger :
            larger = num

    # Print smaller and larger in the same order as they are in the given array.