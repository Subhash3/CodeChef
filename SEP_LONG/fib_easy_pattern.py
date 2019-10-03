#!/usr/bin/python3

def fib_easy(N) :
    pattern = [2, 3, 0, 9]

    if N == 1 :
        return 0
    elif N == 2 or N == 3 :
        return 1

    i = 0
    ans = pattern[i]
    num = 4
    while num <= N :
        # print(num, ans)
        ans = pattern[(i)%4]
        i += 1
        num *= 2

    return ans

try :
    T = int(input())
except :
    quit()

for testCase  in range(T) :
    N = int(input())
    print(fib_easy(N))
    