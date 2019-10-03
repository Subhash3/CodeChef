#!/usr/bin/python3

def is_sorted(arr, N) :
    for i in range(N-1) :
        if arr[i] > arr[i+1] :
            return False
    return True

def sort_arr(arr, D, N) :
    swaps = 0
    for i in range(N) :
        if is_sorted(arr, N) :
            return swaps
        to_be_swapped = None
        for j in range(i+1, N) :
            if arr[i] - arr[j] == D :
                if to_be_swapped == None or arr[to_be_swapped] > arr[j] :
                    to_be_swapped = j
        if to_be_swapped == None :
            return -1
        arr[i], arr[to_be_swapped] = arr[to_be_swapped], arr[i]
        # print(arr)
        swaps += 1
    return swaps

try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    N, D = map(int, input().split())
    arr = list(map(int, input().split()))
    swaps = sort_arr(arr, D, N)
    print(swaps)