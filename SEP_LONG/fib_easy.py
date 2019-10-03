#!/usr/bin/python3

from math import log2


def fast_power(x, y) : 
    res = 1
  
    while (y > 0) : 
        if ((y & 1) == 1) : 
            res = res * x
  
        y = y >> 1
        x = x * x
          
    return res

def f(N) : # fibonacci
    prev = 1
    p_prev = 0
    for i in range(N) :
        if i == 0 :
            cur = 0
        elif i == 1 :
            cur = 1
        else :
            cur = (prev + p_prev)%10
            p_prev = prev
            prev = cur
        print(i, cur, cur%10)
    return cur%10

try :
    T = int(input())
except :
    quit()

for testCase in range(T) :
    N = int(input())
    l = 2**(int(log2(N)))
    print(f(l))
