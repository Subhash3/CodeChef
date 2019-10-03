#!/usr/bin/python3

def min_index(arr, N) :
    index = None
    for i in range(N) :
        if index == None or arr[i] < arr[index] :
            index = i
    return index

def get_adjacent_elements(arr, index, N) :
    i = (index + 1) % N
    j = index - 1 # even if index == 0, j becomes -1 which implies last num

    return i, j

def get_min_penalty(arr, N) :
    if N == 2 :
        return arr[0] + arr[1] # Just to save some time
    penalty = 0
    length = N
    for i in range(N -1) :
        # print(arr, penalty)
        minIndex = min_index(arr, length)
        i, j = get_adjacent_elements(arr, minIndex, length)
        if arr[i] < arr[j] :
            smaller = i
        else :
            smaller = j
        new_num  = arr[minIndex] + arr[smaller]
        arr[minIndex] = new_num
        arr.pop(smaller)
        length -= 1
        penalty += new_num
    return penalty  

try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    N = int(input())
    arr = list(map(int, input().split()))
    min_penalty = get_min_penalty(arr, N)
    print(min_penalty)
    