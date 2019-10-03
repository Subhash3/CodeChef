#!/usr/bin/python3

for i in range(int(input())) :
    vals = input().split()
    P1 = int(vals[0])
    P2 = int(vals[1])
    K = int(vals[2])

    if ((P1 + P2)//K) % 2 == 0 :
        print("CHEF")
    else :
        print("COOK")

