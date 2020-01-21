#!/usr/bin/python3

try :
    T = int(input())
except :
    quit()

for testCase in range(T) :
    N, K = map(int, input().split())
    Arr = list(map(int, input().split()))

    for i in range(K) :
        a = Arr[i%N]
        b = Arr[N-(i%N)-1]
        Arr[i%N] = a^b
        print(Arr, i%N, N-(i%N)-1)

    for i in range(N) :
        print(Arr[i], end=' ')
    print()
