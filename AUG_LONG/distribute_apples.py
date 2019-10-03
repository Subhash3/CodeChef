#!/usr/bin/python3

try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    N, K = map(int, input().split())
    if N%(K*K) :
        print("YES")
    else :
        print("NO")
