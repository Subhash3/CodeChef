#!/usr/bin/python3

try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    B = int(input())
    print(int((B**2)/8))