#!/usr/bin/python3

from math import sqrt

MAX_N = 1000001

try :
    T = int(input())
except :
    quit()

for testCase in range(T) :
    factor_frequency = list()
    N = int(input())
    for i in range(MAX_N) :
        factor_frequency.append(0)

    length = 0
    max_star = -1
    for n in input().split() :
        num = int(n)
        length += 1

        star = 0
        if num == 1:
            star = length-1
        else :
            for fact in range(2, int(sqrt(num))+1) :
                print("sqrt: ", int(sqrt(num)))
                if num%fact == 0 :
                    a = fact
                    b = num//fact
                    factor_frequency[a-1] += 1
                    if a != b :
                        factor_frequency[b-1] += 1
            star = factor_frequency[num-1]
            factor_frequency[num-1] += 1
        # print(num, factors_count)
        print(num, end='---')
        for kk in range(MAX_N):
            if factor_frequency[kk] > 0:
                print(kk+1, factor_frequency[kk], end=",", sep="-")
        print()
        if max_star < star :
            max_star = star
    print(max_star)