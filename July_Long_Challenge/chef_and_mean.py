#!/usr/bin/python3

def linear_search(arr, num, N) :
    for i in range(N) :
        if arr[i] == num :
            return i+1
    return "Impossible"

def num_to_remove(arr, N) :
    total = sum(arr)
    avg = total/N

    x = total - (avg * (N-1))
    pos = linear_search(arr, x, N)
    return pos

try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    N = int(input())
    A = list(map(int, input().split()))
    num = num_to_remove(A, N)
    print(num)
    