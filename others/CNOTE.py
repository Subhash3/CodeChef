#!/usr/bin/python3

try :
    T = int(input())
except :
    quit()

for test_case in range(T):
    X,Y,K,N = map(int,input().strip().split())
    required = X - Y
    flag = False
    for i in range(N):
        P, C = map(int,input().strip().split())
        if required > 0:
            if P >= required and C <= K:
                flag = True
    if flag :
        print('LuckyChef')
    else:
        print('UnluckyChef')
        