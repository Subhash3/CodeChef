#!/usr/bin/python3

def get_max(A, B, N) :
    Max = None
    for i in range(N) :
        score = 20*A[i]-10*B[i]
        if Max == None or Max < score :
            Max = score
    return Max

try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Max = get_max(A, B, N)
    if Max < 0 :
        Max = 0
    print(Max)
