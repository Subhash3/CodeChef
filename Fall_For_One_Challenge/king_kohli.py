#!/usr/bin/python3

try:
    t = int(input())
except :
    quit()

for test in range(t) :
    N = int(input())
    binary = bin(N)[2:]
    if '0' in binary :
        print("Alas")
    else :
        if N == 1 :
            print("0 0")
        else :
            print("1 1")