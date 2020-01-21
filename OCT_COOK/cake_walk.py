#!/usr/bin/python3

def isPossible(N, num, d) :
    # print(N, num, d)
    if N == num :
        return True
    elif num > N :
        return False
    else :
        num *= d
        return isPossible(N, num, 10) or isPossible(N, num, 20)

try :
    T = int(input())
except :
    quit()

for testCase in range(T) :
    N = int(input())
    possible = isPossible(N, 1, 1)
    if possible :
        print("Yes")
    else :
        print("No")
