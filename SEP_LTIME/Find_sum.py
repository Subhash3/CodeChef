#!/usr/bin/python3

try :
    T = int(input())
except :
    quit()

for testCase in range(T) :
    N, Q = map(int, input().split())
    B = list(map(int, input().split()))
    for q in range(Q) :
        p, q = map(int, input().split())
        if abs(p -q) %2 == 0 :
            print("UNKNOWN")
        else :
            if p > q :
                m = p
            else :
                m = q
            s = 0
            for i in range(m) :
                s += B[i]
            print(s)