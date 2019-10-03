#!/usr/bin/env python3

import time

def sum_n(N) :
    return int((N*(N+1))/2)

def sum(D, N) :
    result = N
    for i in range(D) :
        print("Computing sum(" + str(N) + ")")
        result = sum_n(N)
        N = result
    return result   

try :
    T = int(input())
except :
    quit()

for i in range(T) :
    D, N = map(int, input().rstrip().split())
    start = time.time()
    print(sum(D, N))
    end = time.time()
    print("Time: ", end-start)
