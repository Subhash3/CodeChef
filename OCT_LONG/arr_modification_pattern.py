#!/usr/bin/python3

try :
    T = int(input())
except :
    quit()

for testCase in range(T) :
    N, K = map(int, input().split())
    Arr = list(map(int, input().split()))

    possible_values = list()

    for i in range(N) :
        a = Arr[i]
        b = Arr[N-(i%N)-1]
        if i < int(N/2) :
            possible_values.append((a^b, b, a))
        else :
            possible_values.append((b, a^b, a))

    print(possible_values)
    for i in range(K) :
        a = Arr[i%N]
        b = Arr[N-(i%N)-1]
        Arr[i%N] = a^b
        print(i+1, Arr, i%N, N-(i%N)-1)
        if i%N == N-1 :
            print()

    for i in range(N) :
        print(Arr[i], end=' ')
    print()
