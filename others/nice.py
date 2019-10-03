#!/usr/bin/env python3

def mod(n) :
    if n > 0 :
        return n
    else :
        return -n

for i in range(int(input())) :
    ints = input().split()
    a = int(ints[0])
    b = int(ints[1])
    n = int(ints[2])
    if n % 2 == 0 :
        if mod(a) > mod(b) :
            print("1")
        elif mod(a) < mod(b) :
            print("2")
        else :
            print("0")
    else :
        if a > b :
            print("1")
        elif a < b :
            print("2")
        else :
            print("0")
