#!/usr/bin/python3

import time

try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    N = int(input())
    K = int(input())

    distribution = list()
    n = N
    k = K
    # start = time.time()
    # # For the sum of differences of adjacent elements to be min
    # # each element of the distribution should be nearst to the adjacent element
    # for i in range(n) :
    #     num = K//N
    #     distribution.append(num)
    #     K -= num
    #     N -= 1
    # print(distribution)
    # print("Time:", time.time() - start)
    # This for loop generates an array of N elements with 2 numbers
    # Let those two numbers are a and b, b = a+1.
    # b = ceil(K//N), a = b-1. let m = K % N.
    # The array contains m b's and N-m a's

    # This loop should do the same.
    N = n # restore N
    K = k
    m = K % N
    b = K//N + 1
    a = b -1
    dist = list()
    start = time.time()
    for j in range(N-m) :
        dist.append(a)
    for i in range(m) :
        dist.append(b)
    print("Time:", time.time() - start)
    print(dist)
    print("Time:", time.time() - start)
