#!/usr/bin/python3

MODULO = 1000000007

import itertools

def mul(arr, n) :
    ans = 1
    for i in range(n) :
        ans = ((ans%MODULO) * (arr[i]%MODULO))%MODULO
    return ans

N, K = map(int, input().split())
Arr = dict()
for num in input().split() :
    num = int(num)
    if num in Arr :
        Arr[num] += 1
    else :
        Arr[num] = 1

ans = N +1
for i in range(2, K+1) :
    combs = itertools.combinations(Arr.values(), i)
    for c in combs :
        prod = mul(c, i)
        ans =  (ans%MODULO + prod%MODULO)%MODULO
        # print(c, i, prod, ans)
print(ans%MODULO)
