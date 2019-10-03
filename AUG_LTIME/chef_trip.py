#!/usr/bin/python3

# works only for k = 2

def check(A, N, A1) :
    for i in range(N) :
        if A[i] == A1[i] :
            pass
        else :
            if A[i] == -1 :
                pass
            else :
                return False
    return True

try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A1 = list()
    A2 = list()
    a = 1
    b = 2
    if K == 2:
        for i in range(N) :
            A1.append(a)
            A2.append(b)
            a, b = b, a

        if check(A, N, A1) :
            print("YES")
            for num in A1 :
                print(num, end=' ')
            print()
        elif check(A, N, A2) :
            print("YES")
            for num in A1 :
                print(num, end=' ')
            print()
        else :
            print("NO")
    else :
        pass        