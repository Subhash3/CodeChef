#!/usr/bin/python3

MODULO = 10**9 +7

def sum_comb(N, p) :
    total = 0
    temp = N
    t = 1
    while True :
        if t >= p :
            break
        # print(temp, N-t, t+1)
        a = temp * (N-t)/(t+1)
        # print(a)
        total += a
        temp = a
        t += 1
    return int(total)

try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    N, M, K = map(int, input().split())
    p = M - N*K
    # print(p)
    if p < 0 :
        print(0)
    elif p == 0 :
        print(1)
    else :
        ans = 1 + N*p + sum_comb(N, p)
        print(ans%MODULO)
        