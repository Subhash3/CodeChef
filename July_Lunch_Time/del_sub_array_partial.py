#!/usr/bin/python3

def is_increasing(A1, i, j, N) :
    for k in range(0, i-1) :
        try :
            if k+1 < i and Arr[k+1] <= Arr[k] :
                # print(Arr[:i]+Arr[j:], "is not increasing")
                return False
        except :
            break
    for k in range(j, N) :
        try :
            if Arr[k+1] <= Arr[k] :
                # print(Arr[:i]+Arr[j:], "is not increasing")
                return False
        except :
            break
    try :
        if i-1 >= 0 and Arr[i-1] >= Arr[j] :
            # print(Arr[:i]+Arr[j:], "is not increasing")
            return False
    except :
        pass
    # print(Arr[:i]+Arr[j:], "is increasing")
    return True

def num_of_ways(Arr, N) :
    ways = 0
    for length in range(1, N) :
        # print("length:", length)
        for i in range(N) :
            try :
                j = i+length
                nice = Arr[j-1]
            except :
                break
            # print(Arr[i:j], i, j)     
            if is_increasing(Arr, i, j, N) :
                ways += 1         

    return ways
try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    N = int(input())
    Arr = list(map(int, input().split()))
    flag = True
    for k in range(N-1) :
        if Arr[k+1] <= Arr[k] :
            flag = False
            break
    if flag :
        ans = (N*(N+1))/2
        print(int(ans)-1)
    else :
        print(num_of_ways(Arr, N))
