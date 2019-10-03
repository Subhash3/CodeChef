#!/usr/bin/python3

def whose_serve(X, Y, K) :
    a = (X+Y)//K

    if a%2 == 0 :
        return "Chef"
    else :
        return "Paja"

try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    X, Y, K = map(int, input().split())
    player = whose_serve(X, Y, K)
    print(player)