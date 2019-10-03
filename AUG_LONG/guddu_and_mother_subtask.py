#!/usr/bin/python3

def xor(A, i, j, k) :
    value1 = A[i]
    for x in range(i+1, j) :
        value1 = value1 ^ A[x]
    value2 = A[j]
    for y in range(j+1, k+1) :
        value2 = value2 ^ A[y]

    return value1 == value2

def get_triads(A, N) :
    count = 0
    for i in range(N) :
        for j in range(i+1, N) :
            for k in range(j, N) :
                if xor(A, i, j, k) :
                    # print(i+1, j+1, k+1)
                    count += 1

    return count

try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    N = int(input())
    A = list(map(int, input().split()))
    ans = get_triads(A, N)
    print(ans)
