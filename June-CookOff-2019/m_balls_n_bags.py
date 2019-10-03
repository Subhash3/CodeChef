#!/usr/bin/python3

def sum_comb(N, p) :
    total = 0
    temp = N
    for t in range(1, p+1) :
        a = temp*(N-t)(t+1)
        total += a
        temp = a
    return total

try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    N, M, K = map(int, input().split())
    p = M - N*K
    if p < 0 :
        print(0)
    else :
        print(1 + N*p + sum_comb(N, p))
        