#!/usr/bin/python3

MODULO = 1000000007

def f(a, b, c) :
    x = 999
    y = -999
    ans = (a-1)*x*x + 2*b*x*y + (c-1)*y*y
    
    return ans

try :
    T = int(input())
except :
    quit()

for testCase in range(T) :
    A, B, C = map(int, input().split())
    count = 0
    for a in range(1, A+1) :
        for b in range(1, B+1) :
            for c in range(1, C+1) :
                l = f(a, b, c)
                if l > 0 :
                    print(a, b, c, l)
                    count = (count%MODULO + 1)%MODULO
    print(count%MODULO)