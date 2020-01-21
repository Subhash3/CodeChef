#!/usr/bin/python3

from math import sqrt

try :
    T = int(input())
except :
    quit()

for testCase in range(T) :
    N  = int(input())
    xor = 0
    for divisor in range(2, int(sqrt(N))+1) :
        if N % divisor == 0 :
            # print(divisor, end=', ')
            xor ^= divisor
            divisor_2 = int(N/divisor)
            if divisor_2 != divisor :
                # print(divisor_2, end=', ')
                xor ^= divisor_2
    xor ^= N
    xor ^= 1
    print(xor)