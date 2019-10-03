#!/usr/bin/python3

def check(S, R, N) :
    S_count = 0
    R_count = 0
    for i in range(N) :
        if S[i] == '1' :
            S_count += 1
        if R[i] == '1' :
            R_count += 1
    if S_count == R_count :
        return True
    else :
        return False
try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    N = int(input())
    S = input()
    R = input()
    if check(S, R, N) :
        print("YES")
    else :
        print("NO")
