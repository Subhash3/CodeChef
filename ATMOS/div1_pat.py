#!/usr/bin/python3

from math import sqrt

MAX_N = 1000000000000000001

precomputed = list()

# for i in range(MAX_N) :
#     precomputed.append(0)

try :
    T = int(input())
except :
    quit()

for testCase in range(T) :
    # N  = int(input())
    for N in range(2, 100) :
        print("N:", N)
        xor = 0
        for divisor in range(2, int(sqrt(N))+1) :
            if N % divisor == 0 :
                # print(divisor, end=', ')
                xor ^= divisor
                divisor_2 = int(N/divisor)
                if divisor_2 != divisor :
                    # print(divisor_2, end=', ')
                    xor ^= divisor_2
            print(xor, end=', ')
        xor ^= N
        xor ^= 1
        print()
        print(N, xor)
        print()
        # precomputed[N-1] = xor
    print("DONE")
