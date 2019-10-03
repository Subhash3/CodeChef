#!/usr/bin/python3

def get_min_penalty(arr, N) :
    if N == 2 :
        return arr[0] + arr[1] # Just to save some time
    penalty = 0
    length = N
    for i in range(N-1) :
        print(arr, penalty)
        min_sum = None
        for i in range(length) :
            total = arr[i] + arr[(i+1)%length]
            if min_sum == None or total <= min_sum :
                a = i
                b = (i+1)%length
                min_sum = total
        penalty += min_sum
        arr[a] = min_sum
        arr.pop(b)
        length -= 1

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
    