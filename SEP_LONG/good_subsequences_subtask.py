#!/usr/bin/python3

MODULO = 1000000007

def c(n, r) :
    if n < r :
        return -1
    if r == 0 :
        return 1
    elif r == 1 :
        return n
    num = 1
    den = 1

    # print("n:", n, "r:", r)
    for i in range(1, r+1) :
        num = ((num%MODULO) * (n%MODULO))%MODULO
        den = ((den%MODULO) * (i%MODULO))%MODULO
        n -= 1
    result = int(num/den)

    return result%MODULO

N, K = map(int, input().split())
Arr = list()
for num in input().split() :
    Arr.append(int(num))
ans = N +1
for r in range(2, K+1) :
    ans = (ans%MODULO + c(N, r)%MODULO)%MODULO
print(ans%MODULO)
