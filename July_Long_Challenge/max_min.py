#!/usr/bin/python3

import time

try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    N = int(input())
    K = int(input())

    m = K % N
    # b = K//N + 1
    # a = b -1
    # dist = list()
    # for i in range(N-m) :
    #     dist.append(a)
    # for i in range(m) :
    #     dist.append(b)
    # print("",a, ":-", N-m, "\n", b, ":-", m)
    # print(dist)
    if N == K :
        print(0)
    elif N == 2 and m == N-m :
        print(1) # 2m -1 or 2(N-m) -1 depends on which is smaller (2m or 2(N-m))
    else :
        if m < N-m :
            ans = 2*(m)
        elif N-m < m: 
            ans = 2*(N-m)
        else : # m = N-m
            ans = 2*m -1
        print(ans)