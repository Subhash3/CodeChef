#!/usr/bin/python3

try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    try :
        N, M = input().split()
        N = int(N)
        M = int(M)
    except :
        quit()
    max_drinks = list(map(int, input().split()))
    fav_flavours = list()
    fav_money = list()
    any_flav = list()
    for i in range(N) :
        D, F, B = input().split()
        fav_flavours.append(int(D))
        fav_money.append(int(F))
        any_flav.append(int(B))