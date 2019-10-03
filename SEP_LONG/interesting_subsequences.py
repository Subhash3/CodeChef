#!/usr/bin/python3

def c(n, r) :
    num = 1
    den = 1
    for i in range(1, r+1) :
        # print(num, den)
        num *= n
        den *= i
        n -= 1
    result = int(num/den)
    return result

def interesting(Arr, N, K) :
    count = 1
    max_num = Arr[K-1]
    flag1 = flag2 = False
    n = 0
    r = 1
    i = K-2
    j = K
    while True :
        if flag1 and flag2 :
            break
        if i >= 0 :
            if Arr[i] == max_num :
                r += 1
            else :
                flag1 = True
        else :
            flag1 = True
        if j < N :
            if Arr[j] == max_num :
                n += 1
            else :
                flag2 = True
        else :
            flag2 = True
        i -= 1
        j += 1
    n += r
    # print("n:", n, "r:", r)
    return c(n, r)

try :
    T = int(input())
except :
    quit()

for testCase in range(T) :
    N, K = map(int, input().split())
    Arr = list()
    flag = True # Are all equal?
    for num in input().split() :
        Arr.append(int(num))
        if int(num) != Arr[0] :
            flag = False
    if N == K :
        print(1)
    elif flag :
        print(c(N, K))
    else :
        Arr = sorted(Arr)
        # print("Sorted arr: ", Arr)
        print(interesting(Arr, N, K))