#!/usr/bin/python3

try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    N, C = map(int, input().split())
    # A = list(map(int, input().split()))
    sum = 0
    for num in input().split() :
        sum += int(num)
    if sum <= C :
        print("Yes")
    else :
        print("No")
